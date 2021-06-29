with open("zadanie51.txt", 'w+') as my_file:
    data_inp = input("Введите несколько строк: \n")
    while data_inp:
        my_file.write(data_inp + '\n')
        data_inp = input()
    my_file.seek(0)
    print("Вы записали в файл следующие строки:", '\n' + my_file.read())