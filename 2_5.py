rating = [8, 8, 7, 5, 5, 5, 4, 2, 1, 1, 1, 1]
print("Существующий рейтинг: ", rating)
elem = input("Введите новое значение: ")
while elem:
    if rating.count(int(elem)) > 0:
        rating.insert(rating.index(int(elem)) + rating.count(int(elem)), int(elem))
        print("Новый  рейтинг: ", rating)
    elif rating[len(rating)-1] > int(elem):
        rating.append(int(elem))
        print("Новый  рейтинг: ", rating)
    else:
        for i in range(len(rating)):
            if rating[i] < int(elem):
                rating.insert(i, int(elem))
                print("Новый  рейтинг: ", rating)
                break
            else:
                continue
    elem = input("Введите новое значение: ")