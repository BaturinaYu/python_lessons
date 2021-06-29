import json

with open("file57.txt", 'r') as f57:
    predpr_dict = dict()
    prib_vsego = 0
    predpr_vsego = 0
    for stroka in f57:
        """Чтобы выделить название фирмы, стоящее в кавычках:"""
        str1 = stroka.split('"')
        """Формируем список из формы собственности, выручки и расходов без символа окончания строки"""
        str2 = str1[2][:-1].split()
        pribil = float(str2[1]) - float(str2[2])
        prib_vsego += pribil if pribil > 0 else prib_vsego
        predpr_vsego += 1 if pribil > 0 else predpr_vsego
        predpr_dict[str1[1]] = pribil
    rez_list = [predpr_dict, {"Средняя прибыль": round(prib_vsego / predpr_vsego, 2) if predpr_vsego > 0 else 0}]
    with open("json57.json", 'w') as jsfile:
        json.dump(rez_list, jsfile)
