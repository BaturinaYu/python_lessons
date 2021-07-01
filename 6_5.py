class Stationery:
    title = "Пишущие принадлежности"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    name = "Ручка"

    def draw(self, color):
        print(f"Рисуем инструментом {self.name}, цвет {color}")


class Pencil(Stationery):
    name = "Карандаш"

    def draw(self, hb):
        print(f"Рисуем инструментом {self.name}, твёрдость {hb}")

class Handle(Stationery):
    name = "Маркер"

    def draw(self, line):
        print(f"Рисуем инструментом {self.name}, наконечник {line}")


st = Stationery()
st.draw()
p = Pen()
p.draw('Синий')
pl = Pencil()
pl.draw('B')
h = Handle()
h.draw('Долото')