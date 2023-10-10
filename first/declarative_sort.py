
# 💡 Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    return numbers.sort(reverse=True)


numbers = [5, 2, 8, 1, 9]
sort_list_declarative(numbers)
print(numbers)  # Выводит [9, 8, 5, 2, 1]