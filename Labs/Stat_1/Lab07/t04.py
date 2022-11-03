# n    k    m
# 12   15
# 15   12
# 15 % 12 = 3
# 12 % 3  = 0
# 3    0


def nsd(n, k):
    if n < k:
        n, k = k, n
    while k > 0:
        n, k = k, n % k
    return n


###### Main ##########

a, b = [int(el) for el in input().split()]
print(nsd(a, b))

