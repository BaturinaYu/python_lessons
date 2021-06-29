with open("zadanie51.txt", 'r', encoding="utf-8") as my_file:
    print("Текст в файле:", '\n' + my_file.read())
    my_file.seek(0)
    strok_v_file = 0
    for st in my_file:
        strok_v_file += 1
        pr_list = st.split()
        print(f"В строке под номером {strok_v_file} количество слов составляет: {len(pr_list)}")
    print(f"Всего строк в файле: {strok_v_file}")