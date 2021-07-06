from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param, sumcalc):
        self.param = param
        self.sumcalc = sumcalc

    @property
    @abstractmethod
    def calculation(self):
        return 1 * self.param + 0

    def __add__(self, other):
        self.sumcalc += self.calculation + other.calculation
        return Suit(-0.3/2, self.sumcalc)

    def __str__(self):
        s_print = f"{self.calculation}"
        self.sumcalc = 0
        return s_print

class Coat(Clothes):
    def __init__(self, param, sumcalc):
        super().__init__(param, sumcalc)

    @property
    def calculation(self):
        return round(self.param / 6.5 + 0.5, 2) if self.sumcalc == 0 else round(self.param / 6.5 + 0.5, 2) + self.sumcalc


class Suit(Clothes):
    def __init__(self, param, sumcalc):
        super().__init__(param, sumcalc)

    @property
    def calculation(self):
        return round(2 * self.param + 0.3, 2) if self.sumcalc == 0 else round(self.param / 6.5 + 0.5, 2) + self.sumcalc

"""Второй параметр для корректировки (скажем на аксессуары из той же ткани), при значении 0 просто хранит сумму"""

coat = Coat(50, 8.19)
print(f"Расчёт ткани на пальто: {coat}")
suit = Suit(1.84, 0)
print(f"Расчёт ткани на костюм: {suit}")
print(f"Общий расчёт: {coat + suit + coat}")
