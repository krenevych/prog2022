def isPrime(k):
    for i in range(2, int(k ** 0.5 + 1)): # Оптимізація
        if k % i == 0:
            return False
    return True

def isSquare(k):
    root = k ** 0.5
    if int(root + 0.5) ** 2 == k:
        return True
    return False

def isPow5(k):
    # 1, 5, 25, 125, 625,
    while k > 1:
        if k % 5 != 0:
            return False
        k = k // 5
    return True

######### Main #############
squares = []
pow5s = []
primes = []
n = int(input("n = "))
for i in range(n):
    a = int(input("a = "))
    if isSquare(a):
        squares.append(a)
    if isPow5(a):
        pow5s.append(a)
    if isPrime(a):
        primes.append(a)

print("Повні квадрати: ", *squares)
print("Степені 5: ", *pow5s)
print("Прості числа: ", *primes)


