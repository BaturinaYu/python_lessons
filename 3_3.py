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


def korr_vvod(arg1):
    while not (float_arg(arg1) or int_arg(arg1)):
        arg1 = input("Введите число в качестве значения: ")
    zn = int(arg1) if int_arg(arg1) else float(arg1)
    return zn


def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    max1 = my_list.pop(my_list.index(max(my_list)))
    max2 = my_list.pop(my_list.index(max(my_list)))
    print(f"Было введено три значения : {arg1}, {arg2}, {arg3}",
          f"Наибольшие два значения: {max1}, {max2}", f"{max1} + {max2} = {max1 + max2}", sep='\n')
    return


zn1 = korr_vvod(input("Введите первое число: "))
zn2 = korr_vvod(input("Введите второе число: "))
zn3 = korr_vvod(input("Введите третье число: "))
my_func(zn1, zn2, zn3)
