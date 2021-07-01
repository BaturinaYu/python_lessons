class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


sotr0 = Position("Иван", "Иванов", "Спецтиалист", {"wage": 20000, "bonus": 10000})
print(f"{sotr0.position}: {sotr0.get_full_name()}, зарплата: {sotr0.get_total_income()}")
sotr1 = Position("Алексей", "Сидоров", "Ведущий спецтиалист", {"wage": 30000, "bonus": 20000})
print(f"{sotr1.position}: {sotr1.get_full_name()}, зарплата: {sotr1.get_total_income()}")
sotr2 = Position("Андрей", "Волков", "Главный спецтиалист", {"wage": 40000, "bonus": 25000})
print(f"{sotr2.position}: {sotr2.get_full_name()}, зарплата: {sotr2.get_total_income()}")
