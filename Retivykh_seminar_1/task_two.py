# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# по сути, сгенерировтаь таблицу истинности

alphabet = [0, 1]
print("X | Y | Z | ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ")
for x in alphabet:
    for y in alphabet:
        for z in alphabet:
            print((f"{x} | {y} | {z} | ",
                   f"{(not (x or y or z)) == ((not x )and (not y) and (not z))}"))
