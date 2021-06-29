with open("predmet.txt", 'r', encoding="utf-8") as file56:
    rez_dict = {}
    for stroka in file56:
        if stroka and stroka.replace(' ', '') != '\n':
            sum_predmet = 0
            k_str = stroka[:stroka.index(':')]
            vsego = 0
            elem = ''
            for sim in stroka[stroka.index(':') + 1:]:
                if sim.isdigit():
                    elem += sim
                elif elem != '':
                    vsego += int(elem)
                    elem = ''
                else:
                    continue
            rez_dict[k_str] = vsego
    print(rez_dict)
