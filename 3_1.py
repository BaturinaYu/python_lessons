"""Функция float_arg проверяет возможно ли представить arg1 в формате действительного числа"""
"""Функция int_arg проверяет возможно ли представить arg1 в формате целого числа"""


def float_arg(arg1):
    rez = True
    try:
        float(arg1)
    except ValueError:
        rez = False
    return rez


def int_arg(arg1):
    rez = True
    try:
        int(arg1)
    except ValueError:
        rez = False
    return rez


"""Функция korr_vvod запрашивает новое значение до тех пор, пока не будет введено число"""


def korr_vvod(arg1):
    while not float_arg(arg1):
        arg1 = input("Введённое значение не является корректным. Введите число: ")
    zn = int(arg1) if int_arg(arg1) else float(arg1)
    return zn


"""Функция chastnoe вычисляет частное arg1 и arg2. При вводе 0 в качестве делителя, выводит предупреждение"""


def chastnoe(arg1, arg2):
    try:
        rezult = arg1 / arg2
    except ZeroDivisionError:
        rezult = "Деление на 0 недопустимо!"
    return rezult


elem1 = korr_vvod(input("Введите делимое: "))
elem2 = korr_vvod(input("Введите делитель: "))
print(f"Были введены числа: {elem1}, {elem2}")
print(f"{elem1} / {elem2} = {chastnoe(elem1, elem2)}")
