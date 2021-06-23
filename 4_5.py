from functools import reduce


def calc_list(arg1, arg2):
    return arg1 * arg2


rez_list = [el for el in list(range(100, 1001)) if el % 2 == 0]
print(reduce(calc_list, rez_list))