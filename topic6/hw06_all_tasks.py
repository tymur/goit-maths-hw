import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sqrt, pi, exp, integrate, lambdify, simplify
from scipy.integrate import quad

# Загальні змінні
x = symbols('x')
a = 9
b = 18

# Символьне визначення функції ефективності
f_sym = 2 * (
    (4 / (1.2 * sqrt(2 * pi))) * exp(-0.5 * ((x - 11) / 1.2)**2) +
    (7 / (2.4 * sqrt(2 * pi))) * exp(-0.5 * ((x - 15) / 2.4)**2)
)

# Побудова графіка функції
f_lambdified = lambdify(x, f_sym, modules=["numpy"])
x_vals = np.linspace(0, 24, 500)
y_vals = f_lambdified(x_vals)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label='Ефективність $f(x)$')
plt.axvspan(a, b, color='orange', alpha=0.2, label='Робочий час (9:00–18:00)')
plt.title('Графік ефективності роботи протягом доби')
plt.xlabel('Час (год)')
plt.ylabel('Кількість завдань/год')
plt.grid(True)
plt.legend()
plt.show()

# Невизначений та визначений інтеграли
indefinite_integral = integrate(f_sym, x)
definite_integral = integrate(f_sym, (x, a, b))

# Чисельні методи
f_numeric = f_lambdified

# Метод прямокутників
def rectangle_method(f, a, b, n=1000):
    h = (b - a) / n
    return sum(f(a + i * h) * h for i in range(n))

# Метод трапецій
def trapezoidal_method(f, a, b, n=1000):
    h = (b - a) / n
    return (h / 2) * (f(a) + 2 * sum(f(a + i * h) for i in range(1, n)) + f(b))

# Метод Сімпсона
def simpson_method(f, a, b, n=1000):
    if n % 2:
        n += 1
    h = (b - a) / n
    return (h / 3) * (f(a) + 4 * sum(f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1))
                      + 2 * sum(f(a + 2 * i * h) for i in range(1, n // 2)) + f(b))

# Метод quad з SciPy
quad_result, _ = quad(f_numeric, a, b)

# Обчислення
rectangle_result = rectangle_method(f_numeric, a, b)
trapezoidal_result = trapezoidal_method(f_numeric, a, b)
simpson_result = simpson_method(f_numeric, a, b)

# Повернення результатів
print(
    simplify(indefinite_integral),
    float(definite_integral),
    rectangle_result,
    trapezoidal_result,
    simpson_result,
    quad_result
)
