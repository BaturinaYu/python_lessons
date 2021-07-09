class MyDate:
    def __init__(self, strdate):
        self.dateint = self.valid(strdate)

    @classmethod
    def transform(cls, param, flag):
        return int(''.join(param)) if flag == '' else flag

    @staticmethod
    def valid(s):
        val_list = s.split('-')
        mass = ''
        if 1 > int(val_list[0]) or int(val_list[0]) > 31:
            mass = 'День месяца принимает значение от 1 до 31'
        elif int(val_list[0]) == 31 and int(val_list[1] in [4, 6, 9, 11]):
            mass = 'В заданном месяце 30 дней'
        elif int(val_list[0]) > 28 and int(val_list[1]) == 2:
            if int(val_list[0]) == 29:
                mass = 'Год не високосный' if int(val_list[2]) % 4 != 0 else mass
            else:
                mass = 'В феврале максимум 28-29 дней'

        mass = mass + '\nМесяц принимает значение от 1 до 12' if 1 > int(val_list[1]) or int(val_list[1]) > 12 else mass
        mass = mass + '\nНекорректное значение года' if len(val_list[2]) != 4 else mass
        val_list[1] = val_list[1].zfill(2)
        return MyDate.transform(val_list, mass)

    def __str__(self):
        return f"{self.dateint}".zfill(8)


date1 = MyDate('7-7-2020')
print(date1)
