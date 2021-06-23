isx_list = [int(el) for el in input("Введите целые числа через пробел: ").split()]
rez_list = [isx_list[i] for i in range(len(isx_list)) if i > 0 and isx_list[i - 1] < isx_list[i]]
print(f"Исходный список: {isx_list}")
print(f"Сформированный список: {rez_list}")
