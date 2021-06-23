from itertools import cycle, count

"""Первый итератор"""

i = 1
for el in count(int(input("Задайте значение: "))):
    if i > 10:
        break
    print(el)
    i += 1

"""Второй итератор"""

isx_list = input("Введите элементы списка через пробел: ").split()
i = 1
for el in cycle(isx_list):
    if i > len(isx_list) * 3:
        break
    print(el)
    i += 1
