

def sum1(N, x):
    s = 1  # S_n
    a = 1  # a_n
    for n in range(1, N + 1):
        a = x / n * a
        s = s + a
    return s


if __name__ == '__main__':
    e = sum1(10, 1)
    print(e)
