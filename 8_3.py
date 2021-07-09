class Proverka(Exception):
    def __init__(self, text):
        self.text = text

rezlist = list()
zn = input("Вводите числа. Чтобы закончить ввод, нажмите Q.\n")
while zn not in ('Q', 'q', 'Й', 'й'):
    try:
        s = zn.replace('.', '').replace('-', '')
        if not s.isdigit():
            raise Proverka('Введено не число!')
        elif s.isdigit() and (zn.count('.') > 1 or zn.count('-') > 1):
            raise Proverka('Введено не число!')
        elif s.isdigit() and zn.count('.') == 1 and (zn[0] == '.' or zn[-1] == '.'):
            raise Proverka('Введено не число!')
        elif s.isdigit() and zn.count('-') == 1 and zn[0] != '-':
            raise Proverka('Введено не число!')
    except Proverka as err:
        print(err)
    else:
        rezlist.append(float(zn)) if float(zn) % 1 != 0 else rezlist.append(int(zn))
    zn = input()

print(f"Результирующий список: {rezlist}")