from tqdm import tqdm
import math
import pandas as pd
from sqlalchemy import create_engine

"""
Если вы дошли до этого файла - вы как минимум разобрались что именно и как мы записываем в фичи. А главное - почему.
Итак, первое что мы делаем - грузим сэмп фичей, в котором содержатся все юзеры
"""

try:
    X = pd.read_csv('C:\\Users\\realn\\PycharmProjects\\ML_training_course\\00_Final_Call\\notebooks_fc_2\\feed_data_sample_3_action.csv')
    print(X.shape)
except Exception as e:
    print(e)

"""
Далее - аплоадер. Это модифицированная версия примера из шага 6.
tqdm - красивый прогресс-бар. Нам очень важно отслеживать, что при аплоаде загрузилась вся таблица. Количество чанков
рассчитывается для правильной работы прогресс бара и именно почанковой загрузки в базу. Что мы там делаем?
Во-первых, переопределяем if_exists на первом и последующих шагах отдельно. Иначе вы никогда не запишете в ту же таблицу
из коробки.
Во-вторых, непосредственно записываем сам чанк, забиваем на индекс (не плодим сущности), method даёт возможность 
вставлять несколько строк в рамках одного инсерта.
"""


def upload_dataframe_in_chunks(data, table_name, engine, chunksize=10000):
    total_chunks = math.ceil(len(data) / chunksize)
    for i in tqdm(range(total_chunks), desc=f"Uploading to {table_name}"):
        chunk = data[i * chunksize : (i + 1) * chunksize]
        if_exists = "replace" if i == 0 else "append"
        chunk.to_sql(table_name, con=engine, if_exists=if_exists, index=False, method="multi")


engine = create_engine(
    "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
    "postgres.lab.karpov.courses:6432/startml"
)

"""
Изначально были опасения в проблемах с памятью при записи в БД, однако на тестах их не словил. Переопределяем размер 
чанка, грузим, идём пить чай. Если уложитесь в 10 минут на 3% изначального df - будет супер. У меня было +-12.
"""
chunksize = 100000
upload_dataframe_in_chunks(X, "igor_makarov_features_lesson_22", engine, chunksize=chunksize)


