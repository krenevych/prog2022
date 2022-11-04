# a) повними квадратами;
def isSquare(k):
    return int(k**0.5) ** 2 == k

# b) степенями п’ятірки;
def isPow5(k):
    # k = 125
    while k > 1:
        if k % 5 != 0:
            return False
        k = k // 5
    return True

# c) простими числами.
def prime(k):
    if k == 1:
        return False

    for i in range(2, k):
        if k % i == 0:
            return False
    return True

####### Main ########
# Дано натуральне число n та послідовність натуральних чисел
# a_1,a_2,...a_n.

squares = []
pow5s = []
primes = []
n = int(input())
for i in range(n):
    a = int(input())
    if isSquare(a):
        squares.append(a)
    if isPow5(a):
        pow5s.append(a)
    if prime(a):
        primes.append(a)

print("Повні квадрати: ", *squares)
print("Степені 5: ", *pow5s)
print("Прості: ", *primes)