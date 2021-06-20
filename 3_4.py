"""Вспомогательные функции проверки на корректность вводимых значений"""


def float_arg(arg1):
    rez = True
    try:
        float(arg1)
    except ValueError:
        rez = False
    if rez and float(arg1) <= 0:
        rez = False
    return rez


def int_arg(arg1):
    rez = True
    try:
        int(arg1)
    except ValueError:
        rez = False
    if rez and int(arg1) >= 0:
        rez = False
    return rez


def korr_vvod1(arg1):
    while not float_arg(arg1):
        arg1 = input("Введите положительное действительное число в качестве первого значения: ")
    return float(arg1)


def korr_vvod2(arg1):
    while not int_arg(arg1):
        arg1 = input("Введите целое отрицательное число в качестве второго значения: ")
    return int(arg1)


"""Функция возведения в степень"""


def my_func(arg1, arg2):
    i = 1
    rez = 1
    j = abs(arg2)
    while i <= j:
        rez /= arg1
        i += 1
    return rez


"""Принимаем аргументы от пользователя и выводим результат выполнения функции"""

x = korr_vvod1(input("Введите положительное действительное число в качестве первого значения: "))
y = korr_vvod2(input("Введите целое отрицательное число в качестве второго значения: "))
print("Были введены значения: ")
print(f"Результат возведения числа {x} в степень {y}: {my_func(x, y)}")
