import random

# Функция вычисления среднего значения массива
def average_value(arr):
    return sum(arr) / len(arr)

# Функция вычисления корреляции Пирсона
def correlation(x, y):
    average_x = average_value(x)
    average_y = average_value(y)
    dividend = sum((x[i] - average_x) * (y[i] - average_y) for i in range(len(x)))
    divider = (sum((xi - average_x)**2 for xi in x) * sum((yi - average_y)**2 for yi in y)) ** 0.5
    return dividend / divider

# Генерируем два массива
x = [random.randint(1, 10) for _ in range(10)]
y = [random.randint(1, 10) for _ in range(10)]
print("x = ", x)
print("y = ", y)

# Вызываем функцию для расчета корреляции Пирсона и выводим результат
print(correlation(x, y))