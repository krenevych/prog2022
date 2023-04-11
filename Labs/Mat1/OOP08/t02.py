if __name__ == '__main__':
    N = int(input("N = "))

    S = 1

    for n in range(2, N+1):
        S = S + 1/n

    print(S)
