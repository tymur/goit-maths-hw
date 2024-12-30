import numpy as np

# Матриця коефіцієнтів заданих рівнянь системи
A = np.array([
    [-1, 1, 2],
    [0, -2, -3],
    [4, -3, 2]
])

# Вектор вільних членів 
B = np.array([1, -4, 7])

def solve_inv_matrix(A, B, verbose=False):
    """
    Розв'язання системи рівнянь матричним методом через обернену матрицю.
    """
    # Обчислення оберненої матриці
    A_inv = np.linalg.inv(A)
    
    # Знаходимо розв'язок
    solution = np.dot(A_inv, B)
    
    if verbose:
        print("Обернена матриця:")
        print(A_inv)
    
    return solution

def solve_cramer(A, B, verbose=False):
    """
    Розв'язання системи рівнянь методом Крамера.
    """
    # Основний визначник
    delta = np.linalg.det(A)
    
    if delta == 0:
        raise ValueError("Система не має єдиного розв'язку (визначник = 0).")
    
    solutions = []
    
    # Обчислення визначників для кожної змінної
    for i in range(A.shape[1]):
        A_i = A.copy()
        A_i[:, i] = B  # Замінюємо i-й стовпець на вектор B
        delta_i = np.linalg.det(A_i)
        delta_i = round(delta_i, 2)
        solutions.append(delta_i / delta)
        
        if verbose:
            print(f"Визначник для змінної {i + 1}: {delta_i}")
    
    return np.array(solutions)

# Використання матричного методу (виклик функції та виведення результату)
solution_inv = solve_inv_matrix(A, B, verbose=True)
print(f"Розв'язок (матричний метод): {solution_inv}")

# Використання методу Крамера (виклик функції та виведення результату)
solution_cramer = solve_cramer(A, B, verbose=True)
print(f"Розв'язок (метод Крамера): {solution_cramer}")
