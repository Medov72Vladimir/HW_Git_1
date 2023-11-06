# procedure paradigm
def multiplication_table(n):
    # Генерация таблицы умножения
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} * {j} = {i*j}")

# Вывод таблицы умножения на экран
n = int(input("Введите число: "))
multiplication_table(n)

"""
Выбор процедурной парадигмы для данной задачи обоснован тем, 
что она позволяет разбить решение на последовательность шагов, 
каждый из которых выполняет определенную функцию. В данном случае, 
это можно разделить на два этапа: генерация таблицы умножения и вывод ее на экран.
"""