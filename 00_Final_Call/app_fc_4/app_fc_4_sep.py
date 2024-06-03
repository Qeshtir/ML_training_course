import os
from catboost import CatBoostClassifier
import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm
from typing import List
from fastapi import FastAPI
# from schema import PostGet
from datetime import datetime
from pydantic import BaseModel
import pydantic

"""
Дисклеймер - я понимаю, что комментарии в промышленной разработке не должны быть такими, как написаны здесь.
Они должны обладать точностью, краткостью, ёмкостью. Однако, т.к. это учебный пример, я решил сделать максимально 
простые для понимания самой широкой аудитории комментарии.
Итак, мы в сервисе. Первое упрощение - добавление модели PostGet локально. Понятно, что в настоящем приложении следовало
бы инициировать папку как модуль, создать схему, дб коннект и т.д. Но здесь попробуем пока максимально простую 
реализацию.
Для начала загрузим модель:
"""


def get_model_path(path: str) -> str:
    if os.environ.get("IS_LMS") == "1":  # проверяем где выполняется код в лмс, или локально.
        MODEL_PATH = '/workdir/user_input/model'
    else:
        MODEL_PATH = path
    return MODEL_PATH


def load_models():
    model_path = get_model_path("cbm_best_balanced.cbm")
    from_file = CatBoostClassifier()
    model = from_file.load_model(model_path, format='cbm')
    return model


# Это функции для вычитки признаков. Чанки поменьше, чтобы щадить память, размер записанной таблицы в total_rows.
# tqdm рисует красивый прогресс бар при запуске кода, чтобы не было ощущения, что загрузка повисла. Найдено в интернете
# Итоговое количество рядов можно было бы передать с каждой загружаемой таблицей, т.к. во время аплоада эта информация
# известна. Но для отладки эта красота не пригодилась, т.к. две из трёх таблиц загружаются моментально.

def batch_load_sql(query: str) -> pd.DataFrame:
    CHUNKSIZE = 100000
    total_rows = 9000000
    engine = create_engine(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
        "postgres.lab.karpov.courses:6432/startml"
    )
    conn = engine.connect().execution_options(stream_results=True)

    chunks = []
    with tqdm(total=total_rows, desc="Loading data") as pbar:
        for chunk_dataframe in pd.read_sql(query, conn, chunksize=CHUNKSIZE):
            chunks.append(chunk_dataframe)
            pbar.update(CHUNKSIZE)

    conn.close()

    return pd.concat(chunks, ignore_index=True)


def load_like_table() -> pd.DataFrame:
    query = 'SELECT * FROM "igor_makarov_features_22_like_table"'
    return batch_load_sql(query)


def load_users_table() -> pd.DataFrame:
    query = 'SELECT * FROM "igor_makarov_features_22_user_table"'
    return batch_load_sql(query)


def load_post_table() -> pd.DataFrame:
    query = 'SELECT * FROM "igor_makarov_features_22_post_table"'
    return batch_load_sql(query)

# Собственно, сама механика предсказаний с пояснениями

def predict_posts(user_id: int, time: datetime, limit: int, like_table, data_post_fin, users_table, from_file):
    # Будем уверенными, что переданная в методе дата подходит для выбранного нами формата
    f = pd.to_datetime(time)
    f = (f - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

    # Найдём юзера
    test_user = users_table[users_table['user_id'] == user_id]

    # Найдём посты, которые нужно для юзера исключить
    excluded_posts = like_table[like_table['user_id'] == user_id]
    excluded_posts = excluded_posts[excluded_posts['timestamp'] < f]['post_id']

    # Исключим посты из общего пула
    posts_fin = data_post_fin.merge(excluded_posts, indicator=True, how='left').loc[
        lambda x: x['_merge'] != 'both'].drop(columns=['_merge'])

    # Подмержим юзера, нужно для предикта
    user_fin = pd.merge(posts_fin, test_user, how="cross")

    # Сделаем предикт
    user_probas = pd.concat([user_fin,
                             pd.Series(from_file.predict_proba(user_fin)[:, 1], index=user_fin.index, name='probas')],
                            axis=1)
    # Выберем топ, вернём списком
    post_list = list(user_probas.sort_values('probas', ascending=False).iloc[:limit]['post_id'])

    return post_list



# Хорошая практика логировать в терминал информацию о загрузке таблиц. Зачем загружаются эти таблицы?
# Всё просто - нам нужно утащить тексты всех возможных постов, чтобы склеить их в ответ метода. Здесь два метода.
# Первый именно загружает таблицу с постами. Второй - отбирает нужные по передаваемому листу.
def load_post_texts_df():
    global post_texts_df
    print("Загружаю все тексты постов...")
    query = "SELECT * FROM post_text_df"
    engine = create_engine(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
        "postgres.lab.karpov.courses:6432/startml"
    )
    post_texts_df = pd.read_sql(query, con=engine)
    print("Все тексты постов успешно загружены в память.")


def load_post_texts(post_ids: List[int]) -> List[dict]:
    global post_texts_df
    if post_texts_df is None:
        raise ValueError("Таблица с текстами постов не загружена. Сначала вызовите функцию load_post_texts_df().")

    # Извлекаем записи из памяти
    records_df = post_texts_df[post_texts_df['post_id'].isin(post_ids)]
    # Зачем тут словарь? Просто потому, что нам нужно заменять post_id на id в ответе метода, а проще всего это сделать
    # циклом через словарь
    return records_df.to_dict("records")

# Загрузим модели и фичи

model = load_models()
print("Модель загружена")
like_table = load_like_table()
print("Лайки загружены")
users_table = load_users_table()
print("Юзеры загружены")
post_table = load_post_table()
print("Посты загружены")
app = FastAPI()
load_post_texts_df()


class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(
        id: int,
        time: datetime,
        limit: int = 5) -> List[PostGet]:
    post_ids = predict_posts(id, time, limit, like_table=like_table, data_post_fin=post_table, users_table=users_table, from_file=model)
    records = load_post_texts(post_ids)

    posts = []
    for rec in records:
        rec["id"] = rec.pop("post_id")  # а вот и смена post_id на id
        try:
            posts.append(PostGet(**rec))
        except pydantic.error_wrappers.ValidationError as e:
            print(f"Validation error for record {rec}: {e}")
    return posts
