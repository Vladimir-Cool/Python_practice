

def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Если массив пустой или содержит только один элемент, он уже отсортирован

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (обычно средний)

    # Разбиваем массив на элементы, меньшие и большие опорного элемента
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортируем подмассивы
    return quicksort(left) + middle + quicksort(right)

list_data = []
# Пример использования
with open("list1000.txt", "r") as file:
    for line in file.readlines():
        list_data.append(int(line[:-1]))

# arr = [3, 6, 8, 10, 1, 2, 1]
print(list_data)
sorted_arr = quicksort(list_data)
print(sorted_arr)