
def rec3(a):
    x3 = 1 # x_n-3
    x2 = 0 # x_n-2
    x1 = 1 # x_n-1
    n = 2
    while x3 <= a:
        n += 1
        x3, x2, x1 = x2, x1, x1 + 2 * x2 + x3
        print(x3, x2, x1)
    return n, x3


if __name__ == '__main__':
    print(rec3(100))
