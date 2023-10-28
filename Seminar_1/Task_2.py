# Отсортировать список его по возрастанию

numbers = [4, 2, 7, 1, 9, 3]

# Императивный подход
sorted_numbers = []
while numbers:
    min_num = min(numbers)
    sorted_numbers.append(min_num)
    numbers.remove(min_num)
print("Отсортированный список:", sorted_numbers)

# Декларативный подход
sorted_numbers = sorted(numbers)
print("Отсортированный список:", sorted_numbers)

# Другой вариант декларативного подхода
numbers.sort()
print("Отсортированный список:", numbers)