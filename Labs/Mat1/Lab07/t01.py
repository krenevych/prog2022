def prime(k):
    if k == 1:
        return False

    for i in range(2, k):
        if k % i == 0:
            return False
    return True


##### Main #######
n = int(input())
for i in range(n, 2*n-1):
    if prime(i) and prime(i+2):
        print(i, i + 2)