class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        return "машина едет"

    def stop(self):
        return "машина остановилась"

    def turn(self, direction):
        if direction == "left":
            rez = "машина повернула налево"
        elif direction == "right":
            rez = "машина повернула направо"
        else:
            rez = "машина едет прямо"
        return rez

    def show_speed(self):
        return f"Скорость составляет {self.speed}км/ч"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, engine):
        super().__init__(speed, color, name, is_police)
        self.engine = engine

    def get_engine(self):
        return self.engine

    def show_speed(self):
        return f"Скорость превышена на {self.speed - 60}км/ч!" if self.speed > 60 else self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, racing):
        super().__init__(speed, color, name, is_police)
        self.racing = racing

    def get_racing(self):
        return self.racing


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, type_car):
        super().__init__(speed, color, name, is_police)
        self.type_car = type_car

    def get_type(self):
        return self.type_car

    def show_speed(self):
        return f"Скорость превышена на {self.speed - 40}км/ч!" if self.speed > 40 else f"Скорость составляет {self.speed}км/ч"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def ispolice(self):
        return "это машина полиции"

print('*' * 20 + "class Car" + '*' * 35)
cl_car = Car(70, "Серый", "Toyota crown", False)
print(f"Характеристики машины {cl_car.name}: цвет {cl_car.color}, скорость {cl_car.speed}")
print(cl_car.go())
print(cl_car.turn("left"))
print(cl_car.turn("right"))
print(cl_car.turn(""))
print(cl_car.show_speed())
print(cl_car.stop())
print('*' * 20 + "class TownCar" + '*' * 35)
cl_tcar = TownCar(70, "Серый", "Toyota crown", False, "бензиновый")
print(f"Характеристики машины {cl_tcar.name}: цвет {cl_tcar.color}, скорость {cl_tcar.speed}")
print(cl_tcar.go())
print(cl_tcar.turn("left"))
print(cl_tcar.turn("right"))
print(cl_tcar.turn(""))
print(cl_tcar.show_speed())
print(cl_tcar.stop())
print('*' * 20 + "class SportCar" + '*' * 35)
cl_scar = SportCar(120, "Красный", "Audi Sport", False, 3.5)
print(f"Характеристики машины {cl_tcar.name}: цвет {cl_tcar.color}, скорость {cl_tcar.speed}")
print(cl_scar.go())
print(cl_scar.turn("left"))
print(cl_scar.turn("right"))
print(cl_scar.turn(""))
print(cl_scar.show_speed())
print(cl_scar.stop())
print(f"Разгоняется с 0 до 100км/ч за {cl_scar.get_racing()}c")
print('*' * 20 + "class WorkCar" + '*' * 35)
cl_wcar = WorkCar(45, "Красный", "Камаз", False, "Грузовик")
print(f"Характеристики машины {cl_wcar.name}: цвет {cl_wcar.color}, скорость {cl_wcar.speed}")
print(cl_wcar.go())
print(cl_wcar.turn("left"))
print(cl_wcar.turn("right"))
print(cl_wcar.turn(""))
print(cl_wcar.show_speed())
print(cl_wcar.stop())
print(f"Тип машины: {cl_wcar.get_type()}")
print('*' * 20 + "class PoliceCar" + '*' * 35)
cl_pcar = PoliceCar(60, "Белый", "Ford", True)
print(f"Характеристики машины {cl_pcar.name}: цвет {cl_pcar.color}, скорость {cl_pcar.speed}")
print(cl_pcar.go())
print(cl_pcar.turn("left"))
print(cl_pcar.turn("right"))
print(cl_pcar.turn(""))
print(cl_pcar.show_speed())
print(cl_pcar.stop())
print(cl_pcar.ispolice())



