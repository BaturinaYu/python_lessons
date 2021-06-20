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


"""Функция iscontfunc проверяет была ли нажата клавиша 'Q' для выхода из программы, а также вычисляет промежуточную 
сумму и общую сумму"""


def iscontfunc(progon, sumzn):
    promsum = 0
    flag = True
    for i in progon:
        if i in ['q', 'Q', 'й', 'Й']:
            flag = False
            break
        elif int_arg(i):
            promsum += int(i)
        elif float_arg(i):
            promsum += float(i)
        else:
            continue
    sumzn += promsum
    return flag, promsum, sumzn


"""Основная функция"""


def suminput():
    print("Вводите числа через пробел. Если хотите завершить выполнение программы, нажмите Q.")
    flag = True
    sumzn = 0
    while flag:
        prom_list = input().split()
        if prom_list != "":
            flag, promsum, sumzn = iscontfunc(prom_list, sumzn)
            print(f"Промежуточная сумма чисел в строке: {promsum}")
            print(f"Общая сумма чисел: {sumzn}")
    print(f"Итоговая сумма чисел: {sumzn}")
    return


suminput()
