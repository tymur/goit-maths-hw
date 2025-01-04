import numpy as np

# Задані вектори
a = np.array([1, 2, 3, 4, 5])
b = np.array([1/2, 1, 2, 3, 4])

# Сума векторів
sum_ab = a + b
print(f"Сума векторів a і b: {sum_ab}")

# Різниця векторів
diff_ab = a - b
print(f"Різниця векторів a і b: {diff_ab}")

# Сума a та транспонованого b
sum_a_b_T = a + b.T
print(f"Сума векторів a і b^T: {sum_a_b_T}")

# Матричний добуток (dot product) a та b
dot_product_ab = np.dot(a, b)
print(f"Матричний добуток (dot product) a і b: {dot_product_ab}")

# Матричний добуток a та транспонованого b
dot_product_a_b_T = np.dot(a, b.T)
print(f"Матричний добуток a і b^T: {dot_product_a_b_T}")

# Добуток Адамара (Hadamard product)
hadamard_product = a * b
print(f"Добуток Адамара (Hadamard product) a і b: {hadamard_product}")

# Ділення a на b
division_ab = a / b
print(f"Ділення a на b: {division_ab}")

# Ділення b на a
division_ba = b / a
print(f"Ділення b на a: {division_ba}")
