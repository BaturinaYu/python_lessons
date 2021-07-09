class ExDivZero(Exception):
    def __init__(self, textex):
        self.textex = textex


class Perehvat():
    def __init__(self, zn):
        self.zn = zn

    def __truediv__(self, other):
        if other.zn == 0:
            raise ExDivZero('Ошибка деления на ноль!')
        return self.zn / other.zn


num = input("Введите два числа: ")
num_list = list(map(int, num.split()))
zn1 = Perehvat(num_list[0])
zn2 = Perehvat(num_list[1])
try:
    rez = zn1 / zn2
except ExDivZero as err:
    print(err)
else:
    print(rez)
