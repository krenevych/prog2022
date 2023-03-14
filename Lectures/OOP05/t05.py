def fact():  # n: 0, 1, 2, 3, 4
    yield 1  # 0!
    f = 1
    k = 1
    while True:
        f = f * k
        k += 1
        yield f


if __name__ == '__main__':
    for i in fact():
        if i >= 1_000_000:
            break
        print(i)
