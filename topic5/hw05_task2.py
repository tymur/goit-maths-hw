import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Аналітична частина
x = sp.symbols('x')
f = -3 * x**2 + 30 * x
f_prime = sp.diff(f, x)

# Знаходимо критичні точки (де похідна = 0)
critical_points = sp.solve(f_prime, x)
maximum_point = critical_points[0]  # одна критична точка

# Обчислюємо значення функції у точці максимуму
y_max = f.subs(x, maximum_point)

# Візуалізація
x_vals = np.linspace(0, 15, 400)
f_lambd = sp.lambdify(x, f, modules='numpy')
f_prime_lambd = sp.lambdify(x, f_prime, modules='numpy')

plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_lambd(x_vals), label='$f(x) = -3x^2 + 30x$', linewidth=2)
plt.plot(x_vals, f_prime_lambd(x_vals), label="$f'(x)$", linestyle='--', color='gray')
plt.scatter([maximum_point], [y_max], color='red', zorder=5, label='Maximum Point')
plt.title('Графік функції та її похідної')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(float(maximum_point), color='red', linestyle=':')
plt.show()

maximum_point, y_max, f_prime
