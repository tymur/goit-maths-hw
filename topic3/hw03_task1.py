import numpy as np

# Задаємо точки
M0 = np.array([0, 0, 0])
M1 = np.array([1, 1/3, 0])
M2 = np.array([0, 2, 1/4])
M3 = np.array([1/2, 1/2, 1])

# Обчислюємо вектори
vec_a = M1 - M0  # Вектор a
vec_b = M2 - M0  # Вектор b
vec_c = M3 - M0  # Вектор c

print(f"Вектор a: {vec_a}")
print(f"Вектор b: {vec_b}")
print(f"Вектор c: {vec_c}")

# Об'єм паралелепіпеда
volume = abs(np.dot(vec_a, np.cross(vec_b, vec_c)))
print(f"Об'єм паралелепіпеда: {volume}")

# Площа поверхні паралелепіпеда
def vector_norm(v):
    return np.linalg.norm(v)

def parallelepiped_surface_area(a, b, c):
    area = 2 * (vector_norm(np.cross(a, b)) + vector_norm(np.cross(a, c)) + vector_norm(np.cross(b, c)))
    return area

surface_area = parallelepiped_surface_area(vec_a, vec_b, vec_c)
print(f"Площа поверхні паралелепіпеда: {surface_area}")

# Кути між векторами
def angle_between_vectors(u, v):
    cos_theta = np.dot(u, v) / (vector_norm(u) * vector_norm(v))
    theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # Радіани
    return np.degrees(theta)  # Перетворюємо в градуси

angle_ab = angle_between_vectors(vec_a, vec_b)
angle_ac = angle_between_vectors(vec_a, vec_c)
angle_bc = angle_between_vectors(vec_b, vec_c)

print(f"Кут між a і b: {angle_ab:.2f} градусів")
print(f"Кут між a і c: {angle_ac:.2f} градусів")
print(f"Кут між b і c: {angle_bc:.2f} градусів")

# Координати решти вершин
M4 = M0 + vec_b + vec_c
M5 = M0 + vec_a + vec_c
M6 = M0 + vec_a + vec_b
M7 = M0 + vec_a + vec_b + vec_c

print(f"Координати M4: {M4}")
print(f"Координати M5: {M5}")
print(f"Координати M6: {M6}")
print(f"Координати M7: {M7}")