# Задача 3: Сортировка слиянием

# ● Контекст
# Ещё один известный и довольно эффективный алгоритм
# сортировки массива - сортировка слиянием (merge sort).
# Алгоритм делится на два этапа:
# ○ этап разбиения - массив разбивается на пару
# массивов до тех пор пока, полученные массивы не
# станут массивами длины 1 (состоящими из одного
# элемента).
# ○ этап слияния - соединяем пары массивов в большие
# массивы так, чтобы полученные массивы были
# отсортированы.
# ● Ваша задача
# Реализовать сортировку слиянием на любом языке в любой
# парадигме. На вход ваша программа получает массив из
# чисел, а вернуть должна отсортированный массив.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно применяем сортировку слиянием к каждой половине
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Слияние двух отсортированных половин
    sorted_arr = merge(left_half, right_half)

    return sorted_arr


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Сравниваем элементы двух половин и добавляем их в результирующий массив
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы из левой половины
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Добавляем оставшиеся элементы из правой половины
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


arr = [9, 5, 2, 7, 1, 8, 3, 6, 4]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)

