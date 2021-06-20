"""Функция int_func проверяет состоит ли слово только из маленьких латинских букв и возвращает его же с заглавной
первой буквой"""


def int_func(arg1):
    flag = True
    for i in arg1:
        if ord(i) < 97 or ord(i) > 122:
            flag = False
            break
    rez = arg1.title() if flag else "Строка не соответствует заданным критериям."
    return rez


my_str = input("Введите слово, состоящее из маленьких латинских букв: ")
print(int_func(my_str))
