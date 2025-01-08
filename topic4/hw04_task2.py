# Задання даних
P = 18  # Python
C = 19  # C++
J = 21  # Java
P_C = 10  # Python і C++
P_J = 7   # Python і Java
C_J = 8   # C++ і Java
total_programmers = 40
none_languages = 3  # Ті, що не знають жодної мови

# Кількість тих, хто знає принаймні одну мову
P_union_C_union_J = total_programmers - none_languages

# Розв'язок
x = P_union_C_union_J - (P + C + J - P_C - P_J - C_J)
print(f"Кількість програмістів, які знають усі три мови: {x}")
