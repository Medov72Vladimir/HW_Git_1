# Дан список целых чисел numbers

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Задача 1
# Необходимо написать в императивном стиле процедуру
# для сортировки числа в списке в порядке убывания.
# Алгоритм сортировки пузырьком.

def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

sort_list_imperative(numbers)
print("Отсортированный список:", numbers)


# Задача 2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)
sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список:", sorted_numbers)