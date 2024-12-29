import numpy as np

# Початковий вектор x
x = np.array([[2], [1]])

# 2.1 Зменшення по OX у 2 рази, збільшення по OY у 3 рази
M1 = np.array([[0.5, 0], [0, 3]])
result_1 = M1 @ x
print("2.1 Масштабування (M1):\n", result_1)

# 2.2 Відображення відносно початку координат
M2 = np.array([[-1, 0], [0, -1]])
result_2 = M2 @ x
print("2.2 Відображення відносно початку координат (M2):\n", result_2)

# 2.3 Перенесення на (-3, 1) з використанням однорідних координат
x_h = np.array([[2], [1], [1]])  # Однорідний вектор
M3 = np.array([[1, 0, -3],
               [0, 1, 1],
               [0, 0, 1]])
result_3 = M3 @ x_h
print("2.3 Перенесення (M3):\n", result_3[:2])

# 2.4 Зсув (shear) на 60° по осі OY
shear_y = np.tan(np.radians(60))
M4 = np.array([[1, shear_y], [0, 1]])
result_4 = M4 @ x
print("2.4 Shear по OY на 60° (M4):\n", result_4)

# 2.5 Поворот вектора на 30°
cos_theta = np.cos(np.radians(30))
sin_theta = np.sin(np.radians(30))
M5 = np.array([[cos_theta, -sin_theta],
               [sin_theta, cos_theta]])
result_5 = M5 @ x
print("2.5 Поворот на 30° (M5):\n", result_5)

# 2.6 Об'єднане перетворення з кроків 1, 2, 4, 5
M6 = M5 @ M4 @ M2 @ M1
result_6 = M6 @ x
print("2.6 Об'єднане перетворення (M6):\n", result_6)
