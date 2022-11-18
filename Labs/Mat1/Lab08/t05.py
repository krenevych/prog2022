# n    m     k
# 12   15
# 15 % 12  = 3
# 12 %  3  = 0
#  3 %  0  ...


def nsd(n, m):
    if n < m:
        return nsd(m, n)

    if m == 0:
        return n

    NSD = nsd(m, n % m)
    return NSD


######### Main #########
a, b = [int(el) for el in input().split()]
print(nsd(a, b))