import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Оголошуємо змінну
x = sp.symbols('x')

# Визначаємо функцію f(x)
f = 2 * ((4 / (1.2 * sp.sqrt(2 * sp.pi))) * sp.exp(-1/2 * ((x - 11) / 1.2)**2) + 
         (7 / (2.4 * sp.sqrt(2 * sp.pi))) * sp.exp(-1/2 * ((x - 15) / 2.4)**2))

# Аналітичний невизначений інтеграл
indefinite_integral = sp.integrate(f, x)

# Визначений інтеграл на відрізку [a, b]
a, b = 9, 18
definite_integral = sp.integrate(f, (x, a, b))

# Побудова графіка функції на відрізку [0, 24]
f_lambdified = sp.lambdify(x, f, 'numpy')
x_vals = np.linspace(0, 24, 400)
y_vals = f_lambdified(x_vals)

plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axvline(x=a, color='gray', linestyle='--', label='a = 9')
plt.axvline(x=b, color='gray', linestyle='--', label='b = 18')
plt.title('Графік функції ефективності роботи')
plt.xlabel('Час доби')
plt.ylabel('Кількість завдань')
plt.legend()
plt.grid(True)
plt.show()

indefinite_integral, definite_integral.evalf()
