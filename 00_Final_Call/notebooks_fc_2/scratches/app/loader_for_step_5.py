import os
from catboost import CatBoostClassifier

import pandas as pd
from sqlalchemy import create_engine

def get_model_path(path: str) -> str:
    if os.environ.get("IS_LMS") == "1":  # проверяем где выполняется код в лмс, или локально. Немного магии
        MODEL_PATH = '/workdir/user_input/model'
    else:
        MODEL_PATH = path
    return MODEL_PATH

def load_models():
    model_path = get_model_path("/00_Final_Call/notebooks_fc_2/catboost_model.cbm")
    from_file = CatBoostClassifier()
    model = from_file.load_model(model_path, format='cbm') # пример как можно загружать модели
    return model



engine = create_engine(
    "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
    "postgres.lab.karpov.courses:6432/startml"
)

df = pd.DataFrame({'user_id' : [1, ..., n], 'feature_1': [n, ..., 1], ...}) # создаем датафрейм исключительно для примера

df.to_sql('my_favourite_table', con=engine) # записываем таблицу

df = pd.read_sql('SELECT * FROM my_favourite_table', con=engine) # считываем таблицу