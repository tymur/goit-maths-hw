import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Створення ортонормованого базису
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])


# Створення 3D-графіка
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')


# Додавання векторів до графіка
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='Вектор 1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', label='Вектор 2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', label='Вектор 3')


# Налаштування вигляду графіка
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('Вісь X')
ax.set_ylabel('Вісь Y')
ax.set_zlabel('Вісь Z')
ax.set_title('Ортонормований базис у 3D')
ax.legend()


# Відображення графіка
plt.show()
