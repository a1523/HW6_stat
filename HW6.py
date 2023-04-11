# Задача 1
# Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, если выборочная средняя 
# M = 80, а объем выборки n = 256.

import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
from scipy import stats
m = 80
sigma = 16
n = 256
p = 0.95
alpha = 0.05
z = stats.norm.ppf(alpha/2)
(m - z * sigma / np.sqrt(n), m + z * sigma / np.sqrt(n))
# (81.95996398454005, 78.04003601545995)

# Задача 2
# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные 
# данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1. Предполагая, что результаты измерений подчинены нормальному 
# закону распределения вероятностей, оценить истинное значение величины X при помощи доверительного интервала, 
# покрывающего это значение с доверительной вероятностью 0,95.

x = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
x_mean = x.mean()
x_std = x.std(ddof = 1)
x_mean_std = x_std / (np.sqrt(len(x)))

result = t_stat(x_mean, x_mean_std, len(x) - 1, 1 - 0.95, 'two-sided')
print(f"Доверительный интервал: {result}")
# Доверительный интервал: (6.267515851415713, 6.912484148584288)

# Задача 3
# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

a = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
x_1 = np.mean(a)
x_2 = np.mean(b)
delta = x_1 - x_2
n = len(a)
D1 = np.var(a, ddof = 1)
D2 = np.var(b, ddof = 1)

D = (D1 + D2) / 2
SE = np.sqrt(D/n + D/n)

t = stats.t.ppf(0.975, 2 * (n - 1))

result = (delta - t*SE, delta + t*SE)
print(f"Доверительный интервал: {result}")
# Доверительный интервал: (-10.068418034506857, 6.268418034506846)