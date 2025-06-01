import numpy as np

# Функція ефективності (зважена сума двох нормальних розподілів)
def efficiency_function(x):
    term1 = (4 / (1.2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 11) / 1.2) ** 2)
    term2 = (7 / (2.4 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 15) / 2.4) ** 2)
    return 2 * (term1 + term2)

# Метод Сімпсона
def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1  # n має бути парним
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
    return h / 3 * S

# Обчислення
a = 9
b = 18
n = 100  # кількість підінтервалів (парна)

integral_value = simpsons_rule(efficiency_function, a, b, n)
print(integral_value)
