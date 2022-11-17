# n    m     k
# 12   15
# 15 % 12  = 3
# 12 %  3  = 0
#  3 %  0  ...


def func(n, m):
    if n < m:
        return func(m, n)

    if m == 0:
        return n

    return func(m, n % m)


######### Main #########
a, b = [int(el) for el in input().split()]
print(func(a, b))