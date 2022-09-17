# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

alphabet = [0, 1]
# по сути, сгенерировтаь таблицу истинности

print("X | Y | Z | ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z " )

for x in alphabet:
	for y in alphabet:
		for z in alphabet:
			print(f"{x} | {y} | {z} | {(not (x or y or z)) == ((not x )and (not y) and (not z))}")