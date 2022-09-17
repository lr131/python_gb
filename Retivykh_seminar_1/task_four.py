# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input())

if 0 < quarter < 5:
	if quarter == 1:
		print("x > 0, y > 0")
	elif quarter == 2:
		print("x < 0, y > 0")
	elif quarter == 3:
		print("x < 0, y < 0")
	if quarter == 4:
		print("x > 0, y < 0")
else:
	print("в двумерном пространстве нет четвертей с таким номером")