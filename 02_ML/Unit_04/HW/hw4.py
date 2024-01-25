import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

data.head()

from sklearn.linear_model import LinearRegression

X = data.drop('target', axis=1)
Y = data['target']

model = LinearRegression()
model.fit(X, Y)

for column, coef in zip(X.columns, model.coef_):
    print(column, coef)

print(model.intercept_)

class GradientDescentMse:
    """
    Базовый класс для реализации градиентного спуска в задаче линейной МНК регрессии
    """

    def __init__(self, samples: pd.DataFrame, targets: pd.DataFrame,
                 learning_rate: float = 1e-3, threshold=1e-6, copy: bool = True):
        """
        self.samples - матрица признаков
        self.targets - вектор таргетов
        self.beta - вектор из изначальными весами модели == коэффициентами бета (состоит из единиц)
        self.learning_rate - параметр *learning_rate* для корректировки нормы градиента
        self.threshold - величина, меньше которой изменение в loss-функции означает остановку градиентного спуска
        iteration_loss_dict - словарь, который будет хранить номер итерации и соответствующую MSE
        copy: копирование матрицы признаков или создание изменения in-place
        """
        ### Your code is here
        self.samples = samples
        self.targets = targets
        self.beta = np.ones(self.samples.shape[1])
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.iteration_loss_dict = dict()
        if copy:
            self.samples = samples.copy()
        else:
            self.samples = samples

    def add_constant_feature(self):
        """
        Метод для создания константной фичи в матрице объектов samples
        Метод создает колонку с константным признаком (interсept) в матрице признаков.
        Hint: так как количество признаков увеличилось на одну, не забудьте дополнить вектор с изначальными весами модели!
        """
        ### Your code is here
        self.samples['interсept'] = 1
        self.beta = np.ones(self.samples.shape[1])

    def calculate_mse_loss(self) -> float:
        """
        Метод для расчета среднеквадратической ошибки

        :return: среднеквадратическая ошибка при текущих весах модели : float
        """
        ### Your code is here
        scalar_value = np.dot(self.samples, self.beta.reshape(-1, 1)).ravel()
        scalar_value = (scalar_value - self.targets).values

        return (np.mean(scalar_value ** 2))

    def calculate_gradient(self) -> np.ndarray:
        """
        Метод для вычисления вектора-градиента
        Метод возвращает вектор-градиент, содержащий производные по каждому признаку.
        Сначала матрица признаков скалярно перемножается на вектор self.beta, и из каждой колонки
        полученной матрицы вычитается вектор таргетов. Затем полученная матрица скалярно умножается на матрицу признаков.
        Наконец, итоговая матрица умножается на 2 и усредняется по каждому признаку.

        :return: вектор-градиент, т.е. массив, содержащий соответствующее количество производных по каждой переменной : np.ndarray
        """

        """result = []
        scalar_value = np.dot(self.samples, self.beta.reshape(-1, 1)).ravel()
        scalar_value = (scalar_value - self.targets).values
        ### Возьмем столбик со значениями 1 признака

        for i in range(len(self.samples.columns)):
            d_i1 = self.samples.values[:, i]

        ### Умножим каждый объект на соответствующее значение признака
            result_value = scalar_value * d_i1
            result = np.append(result, (2 * np.mean(result_value)))
        return result"""
        ### Your code is here

        shift = np.dot(self.samples, self.beta) - self.targets.values
        derivatives = 2 * np.dot(shift, self.samples) / self.samples.shape[0]

        return derivatives

    def iteration(self):
        """
        Обновляем веса модели в соответствии с текущим вектором-градиентом
        """
        ### Your code is here
        self.beta = self.beta - self.learning_rate * (self.calculate_gradient())

    def learn(self):
        """
        Итеративное обучение весов модели до срабатывания критерия останова
        Запись mse и номера итерации в iteration_loss_dict

        Описание алгоритма работы для изменения бет:
            Фиксируем текущие beta -> start_betas
            Делаем шаг градиентного спуска
            Записываем новые beta -> new_betas
            Пока |L(new_beta) - L(start_beta)| > threshold:
                Повторяем первые 3 шага

        Описание алгоритма работы для изменения функции потерь:
            Фиксируем текущие mse -> previous_mse
            Делаем шаг градиентного спуска
            Записываем новые mse -> next_mse
            Пока |(previous_mse) - (next_mse)| > threshold:
                Повторяем первые 3 шага
        """
        ### Your code is here
        start_betas = self.beta
        previous_mse = self.calculate_mse_loss()
        self.iteration()
        next_mse = self.calculate_mse_loss()
        new_betas = self.beta
        while abs(np.linalg.norm(new_betas) - np.linalg.norm(start_betas)) > self.threshold:
            previous_mse = self.calculate_mse_loss()
            start_betas = self.beta
            self.iteration()
            new_betas = self.beta
            next_mse = self.calculate_mse_loss()
            self.iteration_loss_dict[len(self.iteration_loss_dict)] = next_mse
        """while abs(previous_mse - next_mse) > self.threshold:
            previous_mse = self.calculate_mse_loss()

            self.iteration()
            next_mse = self.calculate_mse_loss()
            self.iteration_loss_dict[len(self.iteration_loss_dict)] = next_mse"""

GD = GradientDescentMse(samples=X, targets=Y)
GD.add_constant_feature()
GD.learn()
print('Веса модели при переменных d1, d2, ..., d10 равны соответственно: \n\n' + str(GD.beta))
#print(f'iteration_loss_dict:{(GD.iteration_loss_dict.items())}')
