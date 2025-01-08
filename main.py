from itertools import product

# Усі можливі комбінації значень A, B, C
combinations = list(product([True, False], repeat=3))

print("A | B | C | ¬C | B ∧ ¬C | A ⇔ (B ∧ ¬C)")
print("-" * 39)
for A, B, C in combinations:
    not_C = not C             # Обчислення ¬C
    B_and_not_C = B and not_C # Обчислення B ∧ ¬C
    result = A == B_and_not_C # Обчислення A ⇔ (B ∧ ¬C)
    print(f"{A} | {B} | {C} |  {result}")
