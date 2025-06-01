import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Оголошуємо змінну
x = sp.Symbol('x')

# Визначаємо функції
f1 = x**3 / 3 + x**2 / 2 - 2 * x
f2 = sp.sqrt(x**2 + 1)
f3 = 1 / sp.sqrt(x**2 + 1)

# Обчислюємо похідні
df1 = sp.diff(f1, x)
df2 = sp.diff(f2, x)
df3 = sp.diff(f3, x)

# Обчислюємо значення похідних у точках x = 1 і x = -1/2

# Варіант 1 - в одному циклі, виводимо результати для всіх функцій по першій точці, а потім для всіх функцій по другій. 
values = {}
for val in [1, -1/2]:
    values[val] = {
        "f1'": df1.subs(x, val).evalf(),
        "f2'": df2.subs(x, val).evalf(),
        "f3'": df3.subs(x, val).evalf()
    }

df1, df2, df3, values
print(values)

# Варіант 2 - для кожної функції в циклі проганяємо обидва значення х в заданних точках, виводимо відповідно 2 результати для кожної функції
points = [1, -1/2]

results = {
    'f1': {p: df1.subs(x, p).evalf() for p in points},
    'f2': {p: df2.subs(x, p).evalf() for p in points},
    'f3': {p: df3.subs(x, p).evalf() for p in points},
}
results
print(results)

# Створюємо масив значень x
x = np.linspace(-2, 2, 400)

# Функції
f1 = (x**3)/3 + (x**2)/2 - 2*x
f2 = np.sqrt(x**2 + 1)
f3 = 1 / np.sqrt(x**2 + 1)

# Похідні
f1_prime = x**2 + x - 2
f2_prime = x / np.sqrt(x**2 + 1)
f3_prime = -x / (x**2 + 1)**(3/2)

# Створюємо графіки (використовував допоміжні ресурси для генерації коду, оскільки ще не дуже розбираюсь у matplotlib.pyplot)
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
fig.suptitle('Функції та їхні похідні')

# Графік f1 і f1'
axs[0, 0].plot(x, f1, label='f1(x)')
axs[0, 0].set_title('f1(x)')
axs[0, 0].grid(True)
axs[0, 1].plot(x, f1_prime, label="f1'(x)", color='r')
axs[0, 1].set_title("f1'(x)")
axs[0, 1].grid(True)

# Графік f2 і f2'
axs[1, 0].plot(x, f2, label='f2(x)')
axs[1, 0].set_title('f2(x)')
axs[1, 0].grid(True)
axs[1, 1].plot(x, f2_prime, label="f2'(x)", color='r')
axs[1, 1].set_title("f2'(x)")
axs[1, 1].grid(True)

# Графік f3 і f3'
axs[2, 0].plot(x, f3, label='f3(x)')
axs[2, 0].set_title('f3(x)')
axs[2, 0].grid(True)
axs[2, 1].plot(x, f3_prime, label="f3'(x)", color='r')
axs[2, 1].set_title("f3'(x)")
axs[2, 1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
