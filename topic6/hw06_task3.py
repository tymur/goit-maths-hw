import numpy as np

# NB! Визначаємо функцію ефективності, визначаючи дві умови як дві окремі функції, а повертаємо результат як суму цих двох доданків, оскільки ця функція - це суміш двох нормальних розподілів.
def efficiency_function(x):
    term1 = (4 / (1.2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 11) / 1.2) ** 2)
    term2 = (7 / (2.4 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 15) / 2.4) ** 2)
    return 2 * (term1 + term2)

# Метод трапецій для чисельного інтегрування
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

# Межі інтегрування
a = 9
b = 18
n = 1000  # Кількість підінтервалів

# Обчислення інтегралу
trapezoidal_result = trapezoidal_rule(efficiency_function, a, b, n)
print(trapezoidal_result)
