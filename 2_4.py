f_stroka = input("Введите несколько слов через пробел: ").split()
for i in range(len(f_stroka)):
    print(f"{i + 1}. {f_stroka[i][:10]}")
