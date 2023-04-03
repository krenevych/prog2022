
eps = 0.000000000000001
def exp(x):
    s = 1  # S_n
    a = 1  # a_n
    n = 0
    while abs(a) >= eps:
        n += 1
        a = x / n * a
        s = s + a

    return s


if __name__ == '__main__':
    e = exp(1)
    print(e)
