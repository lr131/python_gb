from matrix import Matrix
from clothes import Coat, Costume
from cell import Cell


def task1():
    src1 = [[31, 22], [37, 43], [51, 86]]
    src2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
    src3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
    src4 = [[3, 5], [4, 6], [-1, -8]]
    matrix1 = Matrix(src1)
    matrix2 = Matrix(src2)
    matrix3 = Matrix(src3)
    matrix4 = Matrix(src4)
    print("Тип matrix1: ", type(matrix1))
    print(matrix1)
    print("Тип matrix2: ", type(matrix2))
    print(matrix2)
    matrix_res = matrix1 + matrix2
    print('результат сложения матриц выше:')
    print(matrix_res)
    print("Тип matrix_res: ", type(matrix_res))

    print("Тип matrix1: ", type(matrix1))
    print(matrix1)
    print("Тип matrix3: ", type(matrix3))
    print(matrix3)
    matrix_res = matrix1 + matrix3
    print('результат сложения матриц выше:')
    print(matrix_res)
    print("Тип matrix_res: ", type(matrix_res))

    print("Тип matrix2: ", type(matrix2))
    print(matrix1)
    print("Тип matrix3: ", type(matrix3))
    print(matrix3)
    matrix_res = matrix2 + matrix3
    print('результат сложения матриц выше:')
    print(matrix_res)
    print("Тип matrix_res: ", type(matrix_res))

    print("Тип matrix1: ", type(matrix1))
    print(matrix1)
    print("Тип matrix4: ", type(matrix4))
    print(matrix4)
    matrix_res = matrix1 + matrix4
    print('результат сложения матриц выше:')
    print(matrix_res)
    print("Тип matrix_res: ", type(matrix_res))


def task2():
    coat = Coat('Пальто тети Нины', 54)
    costume = Costume('Костюм на свадьбу', 165)
    print(coat)
    print(coat.consumption)
    print(costume.consumption)


def task3():
    cell1 = Cell(12)
    cell2 = Cell(15)
    print(cell1)
    print(type(cell1))
    print(cell1.make_order(5))

    print(cell2)
    print(type(cell2))
    print(cell2.make_order(5))

    print("cell1 + cell2")
    cell_sum = cell1 + cell2
    print(cell_sum)
    print(type(cell_sum))

    print("cell2 - cell1")
    cell_sub = cell2 - cell1
    print(cell_sub)
    print(type(cell_sub))

    print("cell1 * cell2")
    cell_m = cell1 * cell2
    print(cell_m)
    print(type(cell_m))

    print("cell1 / cell2")
    cell_d = cell1 / cell2
    print(cell_d)
    print(type(cell_d))

    print("cell1 // cell2")
    cell_fd = cell1 // cell2
    print(cell_fd)
    print(type(cell_fd))


if __name__ == '__main__':
    task1()
    task2()
    task3()
