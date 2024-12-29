import numpy as np

a = np.array([[1, 2, 3, 4, 5]])
b = np.array([[1/2, 1, 2, 3, 4]])

# Сума
res = a + b
print("Сума:", res)

# Різниця
res = a - b
print("Різниця:", res)

# Поелементний добуток (Адамара)
res = a * b
print("Добуток Адамара:", res)

# Поелементне ділення
res = a / b
print("Поелементне ділення:", res)

# Матричний добуток
res = np.dot(a, b.T)
print("Матричний добуток a та b^T:", res)
