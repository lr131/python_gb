import copy

class Matrix:
    def __init__(self, list_of_lists):
        self.__data = list_of_lists

    def __str__(self):
        res = ''
        for row in self.__data:
            res = res + str(row) + "\n"
        return res

    def __add__(self, other):
        if len(self.__data) != len(other.__data):
            print("Матрицы сложить невоможно! "
                  "Количество строк не совпадают!")
            return
        if len(self.__data[0]) != len(other.__data[0]):
            print("Матрицы сложить невоможно! "
                  "Количество колонок не совпадают!")
            return
        res = copy.deepcopy(self.__data)
        for row in range(len(self.__data)):
            for col in range(len(self.__data[row])):
                res[row][col] = self.__data[row][col] + other.__data[row][col]
        return Matrix(res)
