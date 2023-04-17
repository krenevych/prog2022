def s(k):
    sn = 1
    for k in range(2, k + 1):
        sn = sn + 1 / k
    return sn


if __name__ == '__main__':
    # for n in range(1, 10): # не дуже хороший варіант, бо всередині функції обчислюються одні й ті ж самі значення по багато розів
    #     print(s(n))

    print(s(10))