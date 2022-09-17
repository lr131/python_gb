# 5. Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними
# в 2D пространстве.
# Пример:
# ◦ A (3,6); B (2,1) -> 5,09
# ◦ A (7,-5); B (1,-1) -> 7,21

a_x = float(input())
a_y = float(input())
b_x = float(input())
b_y = float(input())

length = (((b_x - a_x) ** 2) + ((b_y - a_y) ** 2)) ** (1/2)
print("Расстояние: ", round(length, 4))