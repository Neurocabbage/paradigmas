# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
# 💡 Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] < numbers[j + 1]:
                # Обмен значениями
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


numbers = [5, 2, 8, 1, 9]
sort_list_imperative(numbers)
print(numbers)  # Выводит [9, 8, 5, 2, 1]
