from sys import argv

file_name, virabotka, sum_chas, premiya = argv
print(f"Выработка в часах: {virabotka}")
print(f"Оплата одного часа работы: {sum_chas}")
print(f"Сумма премии: {premiya}")
print(f"Размер зарплаты: {float(virabotka) * float(sum_chas) + float(premiya):.2f}")
