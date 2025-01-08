import matplotlib.pyplot as plt
import numpy as np


def draw_vectors(vectors, colors=None, title=None):

    num_vectors = len(vectors)


    if colors is None:
        colors = ['blue'] * num_vectors

    if title is None:
        title = 'Декілька векторів на площині'

    # Створення нового рисунка та осей
    fig, ax = plt.subplots()


    for i in range(num_vectors):
        start_point, end_point = vectors[i]


        # Визначення вектора та його довжини
        vector = np.array([end_point[0] - start_point[0], end_point[1] - start_point[1]])
        length = np.linalg.norm(vector)


        # Нормалізація вектора
        # normalized_vector = vector / length
        normalized_vector = vector


        # Додавання стрілки до осей
        ax.arrow(start_point[0], start_point[1], normalized_vector[0], normalized_vector[1],
                head_width=0.1, head_length=0.1, fc=colors[i], ec=colors[i])


    # Налаштування візуалізації
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)


    # Відображення графіка
    plt.show()


# Приклад використання функції з декількома векторами та кольорами
vectors = [((1, 2), (4, 6)), ((2, 3), (5, 2)), ((0, 0), (-2, 4))]
colors = ['green', 'red', 'purple']


draw_vectors(vectors, colors)
