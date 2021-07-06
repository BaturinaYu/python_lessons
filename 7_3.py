from math import fabs


class Cells:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cells(self.cell + other.cell)

    def __sub__(self, other):
        return Cells(fabs(
            self.cell - other.cell)) if self.cell - other.cell != 0 else "В заданных клетках равное число ячеек. " \
                                                                         "Задайте другие значения."

    def __mul__(self, other):
        return Cells(self.cell * other.cell)

    def __truediv__(self, other):
        return Cells(self.cell // other.cell) if self.cell >= other.cell else Cells(other.cell // self.cell)

    def __str__(self):
        return f"{self.cell:.0f}"

    def make_order(self, count):
        i = self.cell // count
        j = self.cell % count
        rez = '\n'.join('*' * count for el in range(i)) + '\n' + '*' * j
        return rez


exemplar1 = Cells(12)
exemplar2 = Cells(15)
print(f"Сумма: {exemplar1 + exemplar2}")
print(f"Разность: {exemplar1 - exemplar2}")
print(f"Умножение: {exemplar1 * exemplar2}")
print(f"Деление: {exemplar1 / exemplar2}")
print(exemplar2.make_order(5))

