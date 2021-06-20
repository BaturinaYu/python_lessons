

"""Функция vvod проверяет передано ли значение в функцию pers_data, если нет - запрашивает значение у пользователя"""


def pers_data(name="-", surname="-", bornin="-", loc="-", email="-", phone_n="-"):
    def vvod(arg1, arg2):
        zn = input(f"Введите {arg2}: ") if arg1 == "-" else arg1
        return zn

    print(
        f"Имя: {vvod(name, 'имя')}    Фамилия: {vvod(surname, 'фамилию')}    "
        f"Дата рождения: {vvod(bornin, 'дату рождения')}    Город проживания: {vvod(loc, 'город проживания')}"
        f"    e-mail: {vvod(email, 'e-mail')}    Номер телефона: {vvod(phone_n, 'номер телефона')}")
    return


pers_data()
# pers_data(name='Юлия', loc='Елизово')
