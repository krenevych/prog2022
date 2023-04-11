if __name__ == '__main__':
    x = float(input("x = "))
    N = int(input("N = "))

    x_k = 1
    for k in range(1, N + 1):
        x_k = - x / (k * (k+1)) * x_k

    print(x_k)
