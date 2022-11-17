# n    k    m
# 12   15
# 15   12
# 15 % 12 = 3
# 12 % 3  = 0
# 3    0


def nsd(n, k): # n  k
    if n < k:  # 12 15
        return nsd(k, n)

    if k == 0:
        return n

    return nsd(k, n % k)


###### Main ##########

a, b = [int(el) for el in input().split()]
print(nsd(a, b))

