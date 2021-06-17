elem = input("Введите элемент списка: ")
f_list = []
while elem:
    f_list.append(elem)
    elem = input("Введите элемент списка: ")
print("Исходный список: ", f_list)
i = 0
while len(f_list[i:(i + 2)]) != 1 and f_list[i:(i + 2)] != []:
    f_list[i:(i + 2)] = f_list[i:(i + 2)][::-1]
    i += 2
print("Итоговый список: ", f_list)