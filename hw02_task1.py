import numpy as np

# Матриця коефіцієнтів (кількість годин кожного типу спеціалістів)
A = np.array([[20, 3, 0],
              [8, 28, 4],
              [4, 12, 32]])

# Вектор вільних членів (суми, закладені до смети на кожному етапі проекту)
b = np.array([775, 1012, 696])

# Визначник основної матриці
delta = np.linalg.det(A)

# Визначники для x, y, z
A_x = A.copy()
A_x[:, 0] = b
delta_x = np.linalg.det(A_x)

A_y = A.copy()
A_y[:, 1] = b
delta_y = np.linalg.det(A_y)

A_z = A.copy()
A_z[:, 2] = b
delta_z = np.linalg.det(A_z)

# Розв'язок (розрахунок вартості години роботи)
x = delta_x / delta
y = delta_y / delta
z = delta_z / delta

# Округлення вартості
x = round(x, 2)
y = round(y, 2)
z = round(z, 2)

print(f"Вартість години роботи дизайнера - ${x}, розробника - ${y}, а тестувальника - ${z}")
