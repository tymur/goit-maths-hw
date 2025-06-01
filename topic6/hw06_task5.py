import numpy as np
from scipy.integrate import quad

# Функція ефективності (визначена за умовою)
def efficiency(x):
    term1 = (4 / (1.2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 11) / 1.2) ** 2)
    term2 = (7 / (2.4 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 15) / 2.4) ** 2)
    return 2 * (term1 + term2)

# Межі інтегрування
a = 9
b = 18

# Інтегрування функції за допомогою quad
integral_value, error = quad(efficiency, a, b)

print(integral_value, error)

