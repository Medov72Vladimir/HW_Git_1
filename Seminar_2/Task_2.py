
# Переписать алгоритм в процедурном стиле


# Создание функции merge_sort(), которая выполняет сортировку методом слияния и возвращает массив
def merge_sort(array):
    n = len(array) # переменная для хранения длины массива
    temp_array = [0] * n # переменная для хранения временного массива
    size = 1 # переменная для хранения размера блока при слиянии
    while size < n:
        i = 0
        while i < n:
            if i + size < n:
                # функция слияния двух блоков массива
                merge(array, i, i + size - 1, i + size, min(i + 2*size - 1, n-1), temp_array)
            else:
                # функция слияния оставшегося блока массива с последним блоком
                merge(array, i, n - 1, i + size, n - 1, temp_array)
            i += 2*size
        size *= 2
    return array # возвращает отсортированный массив

# Создание функции merge(), которая  выполняет слияние двух отсортированных
# подмассивов (левого и правого) в один отсортированный массив
# и возвращает исходный массив
def merge(array, left_start, left_end, right_start, right_end, temp_array):
    i = left_start # хранит индекс начала левого блока
    j = right_start # хранит индекс начала правого блока
    k = left_start # хранит индекс временного массива
    while i <= left_end and j <= right_end:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            j += 1
        k += 1
    while i <= left_end:
        temp_array[k] = array[i]
        i += 1
        k += 1
    while j <= right_end:
        temp_array[k] = array[j]
        j += 1
        k += 1
    # данный цикл копирует элементы из временного массива в исходный
    for k in range(left_start, right_end+1):
        array[k] = temp_array[k]
    return array # возвращает исходный массив

my_array = [64, 34, 25, 12, 22, 11, 90] # Создание неотсортированного массива.
merge_sort(my_array) # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", my_array) # Вывод отсортированного массива в консоль