def fact(n):
    j = 0
    fact_n = 1
    while j < n:
        j += 1
        fact_n *= j
        yield fact_n, j


for el, i in fact(int(input("Введите целое положительное число: "))):
    print(f"{i}! = {el}")
