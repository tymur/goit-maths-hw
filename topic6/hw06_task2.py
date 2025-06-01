import numpy as np

# Оголошення самої функції f(x)
def f(x):
    return 2 * (
        (4 / (1.2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 11) / 1.2) ** 2) +
        (7 / (2.4 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 15) / 2.4) ** 2)
    )

# Метод прямокутників (лівих)
def rectangle_integral(func, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        total += func(a + i * h)
    return h * total

# Параметри
a = 9
b = 18
n = 1000

# Обчислення
integral_value = rectangle_integral(f, a, b, n)
print(integral_value)
