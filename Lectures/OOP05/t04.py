def fact(n):  # n: 0, 1, 2, 3, 4
    yield 1
    f = 1
    for k in range(1, n + 1):
        f = f * k
        yield f


if __name__ == '__main__':
    # for i in fact(10):
    #     print(i)
    list_factorials = list(fact(10))
    print(list_factorials)
