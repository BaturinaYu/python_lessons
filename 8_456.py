from datetime import date, datetime


class NotInStuff(Exception):
    def __init__(self, text):
        self.text = text


class InvDate(Exception):
    def __init__(self, text) -> object:
        self.text = text

"""Описание класса Склад"""

class Storehouse:
    def __init__(self, specification):
        self.specification = specification

    """Функция меняет статус ячеек со свободной на занятую и обратно"""

    def replace(self, namef, cell, a, aa):
        with open(r"8_456files/" + namef, 'r+', encoding="utf-8") as cells_file:
            result = -1
            ind = 0
            s = '\t0\n' if a == 0 and aa == 1 else f'{cell}\n'
            cells_list = cells_file.readlines()
            for i in cells_list:
                j = i.find(s)
                if j != -1:
                    result = i[:4]
                    ind = cells_list.index(i)
                    break
            if a == 0 and aa == 1:
                cells_list[ind] = cells_list[ind].replace('\t0\n', '\t1\n')
                cells_file.seek(0)
                cells_file.writelines(cells_list)
            elif a == 1 and aa == 0:
                cells_list[ind] = cells_list[ind].replace('\t1\n', '\t0\n')
                cells_file.seek(0)
                cells_file.writelines(cells_list)
        return result

    """Функция производит проверку на наличие свободных ячеек подходящего размера"""

    def place(self, obj):
        namef = 'None'
        result = -1
        if self.specification['Small'][1] > obj.size[0] and self.specification['Small'][2] > obj.size[1] and \
                self.specification['Small'][3] > obj.size[2]:
            namef = 'Small.txt'
        elif self.specification['Middle'][1] > obj.size[0] and self.specification['Middle'][2] > obj.size[1] and \
                self.specification['Middle'][3] > obj.size[2]:
            namef = 'Middle.txt'
        elif self.specification['Big'][1] > obj.size[0] and self.specification['Big'][2] > obj.size[1] and \
                self.specification['Big'][3] > obj.size[2]:
            namef = 'Big.txt'
        if namef != 'None':
            result = self.replace(namef, '', 0, 1)
        return result

    """Функция фиксации поступления на склад, ведёт запись в файл Arrival.txt, если для товара не нашлось 
       свободной ячейки, запись ведётся в файл Err.txt"""

    def arrival(self, objs, pers, dateplace, branch):
        try:
            with open(r"8_456files/Stuff.txt", 'r', encoding="utf-8") as stuff_file:
                if stuff_file.read().find(f'{pers[0]}\t{pers[1]}') == -1:
                    raise NotInStuff("Сотрудника нет в списке работников данного склада!")
            if (datetime.strptime(dateplace, '%Y%m%d').date()) != date.today():
                raise InvDate("Нельзя принять товар за прошедшую дату!")
        except (NotInStuff, InvDate) as err:
            print(err)
        else:
            with open(r"8_456files/Arrival.txt", 'a', encoding="utf-8") as arriv_file:
                with open(r"8_456files/Err.txt", 'w', encoding="utf-8") as err_file:
                    for obj in objs:
                        cell = self.place(obj)
                        if cell != -1:
                            arriv_file.write(f'{cell}\t{obj.art}\t{obj.name}\t{pers[0]}\t{dateplace}\t{branch}\n')
                            print(f'Товар {obj.art} {obj.name} занесён в файл Arrival.txt')
                        else:
                            err_file.write(f'{obj.art}\t{obj.name}\t{pers[0]}\t{dateplace}\t{branch}\n')
                            print(f'Товар {obj.art} {obj.name} занесён в файл Err.txt')

    """Функция формирования списка на отправку в другой филиал, производит проверку наличия товара в списке 
       Arrival.txt"""

    def extract(self, objs, pers, dateex, branch):
        with open(r"8_456files/Arrival.txt", 'r+', encoding="utf-8") as arriv_file:
            with open(r"8_456files/Err.txt", 'w', encoding="utf-8") as err_file:
                cells_list = arriv_file.readlines()
                for obj in objs:
                    ind = -1
                    for i in cells_list:
                        j = i.find(f'\t{obj.art}\t')
                        if j != -1:
                            cell = i[:4]
                            ind = cells_list.index(i)
                            break
                    if ind != -1:
                        with open(r"8_456files/Dispatch.txt", 'a', encoding="utf-8") as disp_file:
                            disp_file.write(f'{obj.art}\t{obj.name}\t{pers[0]}\t{dateex}\t{branch}\n')
                            print(f'Товар {obj.art} {obj.name} занесён в файл Dispatch.txt')
                        if self.specification['Small'][4][1] >= int(cell) >= self.specification['Small'][4][0]:
                            namef = 'Small.txt'
                        elif self.specification['Middle'][4][1] >= int(cell) >= self.specification['Middle'][4][0]:
                            namef = 'Middle.txt'
                        elif self.specification['Big'][4][1] >= int(cell) >= self.specification['Big'][4][0]:
                            namef = 'Big.txt'
                        self.replace(namef, cell, 1, 0)
                    else:
                        err_file.write(f'\nТовар {obj.art} {obj.name} не найден в списке отгрузки')


class Objects:
    def __init__(self, art, name, size):
        self.art = art
        self.name = name
        self.size = size


class Printer(Objects):
    def __init__(self, art, name, size, characteristics):
        super().__init__(art, name, size)
        self.characteristics = characteristics


class MFU(Objects):
    def __init__(self, art, name, size, characteristics):
        super().__init__(art, name, size)
        self.characteristics = characteristics


class Laminator(Objects):
    def __init__(self, art, name, size, characteristics):
        super().__init__(art, name, size)
        self.characteristics = characteristics

"""Объект Склад содержит информацию о ячейках хранения размеров Small, Middle, Big. 
   Для каждой ячейки есть список характеристик: количество ячеек, ширина, высота, глубина и интервал номеров.
   Также хранится список персональных кодов сотрудников склада."""

sh = Storehouse(
    {"Big": [40, 1100, 1100, 900, (1, 40)], "Middle": [60, 800, 800, 800, (41, 100)],
     "Small": [100, 400, 200, 250, (101, 200)],
     "Stuff": ['001', '002', '005']})
prt = Printer('1234568', "Pantum P2200", [337, 178, 220],
              {'ТП': 'лазерная', 'Формат': 'А4', 'Разрешение': '1200х1200dpi', 'Цветная': 'нет'})
mfu = MFU('4564568', "HP LaserJet Pro MFP M28a", [360, 197, 264],
          {'Формат': 'А4', 'Функции': ['принтер', 'сканер', 'копир'],
           'Разрешение': ['1200х1200dpi', '600x600dpi', '600x400dpi'], 'Цветная': 'нет'})
lami = Laminator('7894568', "ГЕЛЕОС ЛМ-А4-2R", [343, 148, 70],
                 {'СЛ': ['горячий', 'холодный'], 'Формат': 'А4', 'Скорость': '300мм',
                  'Толщина плёнки': '150мкм'})
sh.arrival([prt, mfu, lami], ('002', 'Петров Тихон Семёнович'), '20210709', 'Филиал1')
sh.extract([prt, lami], ('005', 'Сидоров Иван Петрович'), '20210709', 'Филиал2')
