# Выбираем четные числа, сортируем и возводим в квадрат.

# Императивно
numbers = [5, 2, 9, 8, 3, 6]
result = []
for num in numbers:
    if num % 2 == 0:  # Проверяем, является ли число четным.
        result.append(num)
result.sort(reverse=True)  # Сортируем по убыванию.
for i in range(len(result)):
    result[i] = result[i] ** 2  # Возводим в квадрат.

# Декларативно
numbers = [5, 2, 9, 8, 3, 6]
result = sorted((x ** 2 for x in numbers if x % 2 == 0), reverse=True)