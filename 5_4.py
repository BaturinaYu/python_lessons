with open("file_ru.txt", 'w') as file_ru:
    with open("file_en.txt", 'r') as file_en:
        for element in file_en:
            j = element.index('-')
            if element[:j] == "One":
                file_ru.write("Один" + element[j:])
            elif element[:j] == "Two":
                file_ru.write("Два" + element[j:])
            elif element[:j] == "Three":
                file_ru.write("Три" + element[j:])
            else:
                file_ru.write("Четыре" + element[j:])
