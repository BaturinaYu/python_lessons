with open("zarplata.txt", 'r', encoding="utf-8") as zp_file:
    count = len(zp_file.readlines())
    zp_file.seek(0)
    sum_zp = 0
    flag = False
    print("Сотрудники с зарплатой менее 20000:")
    for worker in zp_file:
        worker_list = worker.split()
        try:
            zn = float(worker_list[1])
            sum_zp += zn
            if zn <= 20000:
                print(worker_list[0])
                flag = True
        except ValueError:
            print(f"У сотрудника {worker_list[0]} некорректно указан размер дохода!")
    if not flag:
        print("В списке нет сотрудников с доходом менее 20000")
    print(f"Средняя величина дохода сотрудников составляет: {sum_zp / count:.2f}")