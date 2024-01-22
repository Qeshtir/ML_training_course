import pandas as pd
import numpy as np
import loader_u1
from sklearn.linear_model import LinearRegression

pd.pandas.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

data = loader_u1.data_p.copy()
Macro = loader_u1.Macro_p.copy()

print(data.shape)

# нужно выбрать только отменённые и успешные проекты
data = data[data['Состояние'].isin(['failed', 'successful'])]

# и что же вышло
print(data['Состояние'].value_counts())

# создадим колонку таргет1 (бинарный)
data.loc[(data['Состояние'] == 'failed'), 'target1'] = 0
data['target1'] = data['target1'].fillna(1)

# состояние перестало быть информативным
data = data.drop('Состояние', axis=1)

# создадим вещественный таргет2 (сколько денег проект собрал)
data = data.rename({'Собрано в долларах': 'target2'}, axis=1)

# Начнём преобразовывать данные таблицы в более легко обрабатываемые признаки. Начнём с дат.
# Свяжем дедлайн и дату публикации длительностью проекта.
# Изначально строки с датами - string
data['Дедлайн'] = pd.to_datetime(data['Дедлайн'])
data['Дата публикации'] = pd.to_datetime(data['Дата публикации'])
data['Срок'] = (data['Дедлайн'] - data['Дата публикации']).dt.days
data['Год публикации'] = data['Дата публикации'].dt.year
print(data.head())

# Введём характеристику для года - рост или падение котировок нефти
Macro = Macro[['Close_brent', 'dlk_cob_date']].drop_duplicates()
Macro['dlk_cob_date'] = pd.to_datetime(Macro['dlk_cob_date'])
data['Дата публикации'] = data['Дата публикации'].astype('datetime64[ns]')
data = pd.merge(
    data,
    Macro,
    left_on=['Дата публикации'],
    right_on=['dlk_cob_date'],
    how='left'
)

# Значений котировок мало по совпадению даты, заполняем NA сначала предыдущим известным значением,
# а затем все перед первым известным - им же
data = data.sort_values('Дата публикации')
data['Close_brent'] = data['Close_brent'].fillna(method='ffill')
data['Close_brent'] = data['Close_brent'].fillna(46.05)

# удалить мусор
data = data.drop(['Дедлайн', 'Дата публикации', 'dlk_cob_date'], axis=1)

# Удаляем незначимые признаки: название, страна (т.к. она соотносится с валютой),
# инвесторов (не можем знать заранее, выполнится таргет или нет, а количество инвесторов на это влияет,
# хотя в новых проектах инвесторов всегда 0)
data = data.drop(['Название', 'Страна', 'Инвесторов'], axis=1)

# Обработаем категориальные признаки (One-hot encoding)
# Каждая категория становится одной колонкой. Этой колонке выставляется бинарный признак. Дальше категория удаляется.
data = pd.concat((data, pd.get_dummies(data['Валюта'])), axis=1)
data = data.drop(['Валюта'], axis=1)

# снизим размерность категориального признака - AUD будет вычисляться по всем остальным валютам
data = data.drop(['AUD'], axis=1)

# Повторим для главной категории
data = pd.concat((data, pd.get_dummies(data['Главная категория'])), axis=1)
data = data.drop(['Главная категория'], axis=1)

# снизим размерность категориального признака - AUD будет вычисляться по всем остальным валютам
data = data.drop(['Games'], axis=1)

# Для категории One-hot encoding не подойдёт - мы имеем 159-1 категории таким способом.
# Будем делать Mean-target encoding - для каждой категории считаем средний таргет.
# Таким образом появляется новая колонка - счётчик
data['Категория'] = data['Категория'].map(data.groupby(['Категория'])['target2'].mean())

# Определимся с таргетом (оставляем регрессию)
data = data.drop(['target1'], axis=1)

# Данные явным образом разбиваем на выборку и ответы
X = data.drop(['target2'], axis=1)
Y = data['target2']

print(X)
print(Y)

# Предскажем значения линейной регрессией
model = LinearRegression()
model.fit(X, Y)
X['Предсказание'] = model.predict(X)

print(X.head())

# Посчитаем MAE & MSE нашей модели
# Если таргет высокого порядка, мы получим большой MSE
MSE = (((X['Предсказание'] - Y)**2).mean())**0.5  # c корнем - RMSE (ROOT), значение лучше воспринимается человеком
# Много это или мало - зависит от таргета. Чем больше таргет и меньше MSE/RMSE - тем менее значима ошибка.

MAE = abs((X['Предсказание'] - Y)).mean()

X.to_csv("X.csv", sep = ";")
Y.to_csv("Y.csv", sep = ";")


