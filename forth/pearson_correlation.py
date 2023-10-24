import numpy as np
'''
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.

'''

def pearson_correlation(x, y):
    # Проверяем, что оба массива имеют одинаковую длину
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    n = len(x)

    # Рассчитываем сумму элементов массивов
    sum_x = sum(x)
    sum_y = sum(y)

    # Рассчитываем сумму квадратов элементов массивов
    sum_x_sq = sum([i ** 2 for i in x])
    sum_y_sq = sum([i ** 2 for i in y])

    # Рассчитываем сумму произведений элементов массивов
    sum_xy = sum([x[i] * y[i] for i in range(n)])

    # Рассчитываем корреляцию Пирсона
    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt((n * sum_x_sq - sum_x ** 2) * (n * sum_y_sq - sum_y ** 2))

    correlation = numerator / denominator

    return correlation


# Пример использования
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
result = pearson_correlation(x, y)
print(f"Корреляция Пирсона: {result}")
