def isPrime(k):
    if k == 1:
        return False

    for i in range(2, int(k ** 0.5 + 1)): # Оптимізація
        if k % i == 0:
            return False
    return True

def invert(k):
    inv = 0
    while k > 0:
        inv = inv * 10 + k % 10
        k = k // 10
    return inv

######### Main ##################

a, b = [int(el) for el in input().split()]
counter = 0

for i in range(a, b + 1):
    if isPrime(i) and isPrime(invert(i)):
        # print(i)
        counter += 1

print(counter)