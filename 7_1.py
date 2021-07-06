class Matrix:
    def __init__(self, matr_list):
        self.matr_list = matr_list

    def __str__(self):
        s = '\n'.join(' '.join(str(sim) for sim in row) for row in self.matr_list)
        return s

    def normalize(self, other):
        matr1 = self.matr_list
        matr2 = other.matr_list
        lenrows1 = len(matr1)
        lenrows2 = len(matr2)
        lencols1 = len(matr1[0])
        lencols2 = len(matr2[0])
        if lenrows1 > lenrows2:
            for row in list(range(lenrows1 - lenrows2)):
                matr2 += [list(0 for el in matr2[0])]
        elif lenrows1 < lenrows2:
            for row in list(range(lenrows2 - lenrows1)):
                matr1 += [list(0 for el in matr1[0])]
        if lencols1 > lencols2:
            for row in matr2:
                row += list(0 for el in list(range(lencols1 - lencols2)))
        elif lencols1 < lencols2:
            for row in matr1:
                row += list(0 for el in list(range(lencols2 - lencols1)))
        return matr1, matr2

    def __add__(self, other):
        m1, m2 = self.normalize(other)
        rez = list(list(range(len(m1[0]))) for el in range(len(m1)))
        for row in m1:
            rez[m1.index(row)] = list(el + m2[m1.index(row)][row.index(el)] for el in row)
        return Matrix(rez)


matrix1 = Matrix([[3, 4, 5, 6], [6, 7, 1, 2], [9, 10, 2, 2], [13, 14, 5, 5]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
print("Матрица 1:")
print(matrix1)
print("Матрица 2:")
print(matrix2)
print("Сумма матриц 1 и 2:")
print(matrix1 + matrix2)
