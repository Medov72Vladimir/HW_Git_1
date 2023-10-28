# Императивный стиль
N = 10
sum = 0
for i in range(1, N + 1):
    sum += i
print("Сумма чисел от 1 до", N, "равна", sum)

# Декларативный стиль
N = 10
numbers = range(1, N + 1)
total = sum(numbers)
print("Сумма чисел от 1 до", N, "равна", total)