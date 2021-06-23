my_list = [int(el) for el in input("Введите целые числа через пробел: ").split()]
rez_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Список без повторов: {rez_list}")