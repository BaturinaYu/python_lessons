from math import fmod

rez_list = [el for el in list(range(20, 241)) if fmod(el, 20) == 0 or fmod(el, 21) == 0]
print(f"Список чисел, кратных 20 или 21, в интервале от 20 до 240: {rez_list}")