def fact(N):
    an = 1
    for n in range(1, N + 1):
        an = n * an

    return an


def seq2(N, x):
    an = 1
    for n in range(1, N + 1):
        an = x / n * an
    return an

def seq2_gen(N, x):
    an = 1
    yield an
    for n in range(1, N+1):
        an = x / n * an
        yield an


if __name__ == '__main__':

    n = 30
    x = 2
    print("В лоб: ", x ** n / fact(n))

    for e in seq2_gen(n, x):
        print(e)
