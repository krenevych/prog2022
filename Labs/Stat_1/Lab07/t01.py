def isPrime(k):
    if k == 1:
        return False

    for i in range(2, k):
    # for i in range(2, int(k) ** 0.5 + 1): # Оптимізація
        if k % i == 0:
            return False
    return True


####### Main program #############
n = int(input("n = "))
for i in range(n, 2 * n - 1):
    if isPrime(i) and isPrime(i + 2):
        print(i, i + 2)
