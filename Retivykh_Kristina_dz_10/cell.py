class Cell:
    def __init__(self, nucleus: int):
        if nucleus > 0:
            self.nucleus = nucleus
        else:
            raise ValueError('в клетке должны быть ячейки!')

    def __str__(self):
        return f'Количество ячеек клетки {self.nucleus}'

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        return self.nucleus - other.nucleus \
            if (self.nucleus - other.nucleus) > 0 else \
            print('в клетке должны быть ячейки!')

    def __mul__(self, other):
        return Cell(int(self.nucleus * other.nucleus))

    def __truediv__(self, other):
        if round(self.nucleus / other.nucleus) > 0:
            return Cell(round(self.nucleus / other.nucleus))
        else:
            raise ZeroDivisionError("в результирующей клетке "
                                    "должны быть ячейки!")

    def __floordiv__(self, other):
        if self.nucleus // other.nucleus > 0:
            return Cell(self.nucleus // other.nucleus)
        else:
            raise ZeroDivisionError("в результирующей клетке "
                                    "должны быть ячейки!")

    def make_order(self, count):
        rows = (self.nucleus // count) * (("*"*count) + "\n")
        tail = (self.nucleus % count) * "*"
        return f'{rows}{tail}'



