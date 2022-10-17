# 12 15 => nsd(15, 12) = 3

n, m = [int(el) for el in input("n, m = ? ").split()]
if n < m: # відсортуємо змінні n i m так, щоб в змінній n було більше число
    tmp = n; n = m;  m = tmp

# n    m    d
# 15 % 12 = 3
# 12 % 3  = 0
# 3  % 0

N = n; M = m
while m > 0:
    d = n % m
    n = m
    m = d

print("nsd(%d, %d) = %d" % (N, M, n))

# 3x5x7 = 105, 5x7x11 = 385