# Задача 2
# Реализовать процедуру для вычисления MSE на Python в любой парадигме. Программа получает
# на вход два вектора и возвращает число - оценку MSE для этих векторов.

def calculate_mse(Y, Y_pred):
    n = len(Y)
    squared_errors = [(Y[i] - Y_pred[i])**2 for i in range(n)]
    mse = sum(squared_errors) / n
    return mse


Y = [1, 2, 3, 4, 5]
Y_pred = [1.5, 2.5, 3.5, 4.5, 5.5]

mse = calculate_mse(Y, Y_pred)
print("MSE:", mse)