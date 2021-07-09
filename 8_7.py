class ComplexNum:
    def __init__(self, ves, mnim):
        self.ves = ves
        self.mnim = mnim

    def __str__(self):
        return f"{self.ves} + {self.mnim}i"

    def __add__(self, other):
        return ComplexNum(self.ves + other.ves, self.mnim + other.mnim)

    def __mul__(self, other):
        v = self.ves * other.ves - self.mnim * other.mnim
        m = self.ves * other.mnim + self.mnim * other.ves
        return ComplexNum(v, m)


comp1 = ComplexNum(5, -2)
comp2 = ComplexNum(-8, 6)
print(f"Первое комплексное число: {comp1}")
print(f"Второе комплексное число: {comp2}")
print(f"Сумма: {comp1 + comp2}")
print(f"Произведение: {comp1 * comp2}")