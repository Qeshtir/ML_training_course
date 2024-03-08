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
    model_path = get_model_path("/00_Final_Call/notebooks_fc_2/scratches/catboost_model_tf_best.cbm")
    from_file = CatBoostClassifier()
    model = from_file.load_model(model_path, format='cbm')
    return model


# Это функции для вычитки признаков. Чанки поменьше, чтобы щадить память, размер записанной таблицы в total_rows.
# tqdm рисует красивый прогресс бар при запуске кода, чтобы не было ощущения, что загрузка повисла. Найдено в интернете

def batch_load_sql(query: str) -> pd.DataFrame:
    CHUNKSIZE = 100000
    total_rows = 2306849
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


def load_features() -> pd.DataFrame:
    query = 'SELECT * FROM "igor_makarov_features_lesson_22_full"'
    return batch_load_sql(query)

# Собственно, сама механика предсказаний с пояснениями


def predict_posts(user_id: int, limit: int):
    # Фильтруем записи, относящиеся к конкретному user_id
    user_features = features[features.user_id == user_id]

    # исправим баг с фильтрацией лайков
    user_features = user_features[user_features['action'] == 'view']
    user_features = user_features.drop(columns=['action'])

    # Вычисляем вероятности для каждого post_id для конкретного user_id.
    # Расчёт ограничен таблицей с фичами, что является самым большим недостатком этого решения (примеров мало).

    # Второй значимый недостаток - отсутствие учёта количества взаимодействий с постом. Т.е. насколько часто
    # пользователь в принципе взаимодействовал с нашим контентом. Подробнее смотри в README.

    user_features['probas'] = model.predict_proba(user_features.drop('user_id', axis=1))[:, 1]

    # Сортируем по probas в порядке убывания и получаем первые limit записей
    top_posts = user_features.sort_values('probas', ascending=False).iloc[:limit]

    # Возвращаем 'post_id' лучших записей в виде списка
    return top_posts['post_id'].tolist()



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
features = load_features()
print("Данные загружены")
# Загрузим глобальную переменную для хранения данных с текстами постов. Почему глобальную? Ради практики.
load_post_texts_df()


app = FastAPI()


class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(
        id: int,
        #time: datetime,
        limit: int = 5) -> List[PostGet]:
    post_ids = predict_posts(id, limit)
    records = load_post_texts(post_ids)

    posts = []
    for rec in records:
        rec["id"] = rec.pop("post_id")  # а вот и смена post_id на id
        try:
            posts.append(PostGet(**rec))
        except pydantic.error_wrappers.ValidationError as e:
            print(f"Validation error for record {rec}: {e}")
    return posts
