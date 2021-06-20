"""Функция int_func проверяет каждое слово из строки на соответствие условию задачи.
   Функция preobr формирует список из слов исходной строки, где каждое из слов начинается с большой буквы.
   Слова, несоответствующие заданным условиям, не входят в возвращаемый список."""


def int_func(arg1):
    flag = True
    for i in arg1:
        if ord(i) < 97 or ord(i) > 122:
            flag = False
            break
    rez = arg1.title() if flag else ""
    return rez


def preobr(arg1):
    pr_list = arg1.split()
    it_list = []
    for i in pr_list:
        elem = int_func(i)
        if elem != "":
            it_list.append(elem)
    return it_list


my_str = input("Введите строку, состоящую из маленьких латинских букв, разделенных пробелом: ")
print(' '.join(preobr(my_str)))
