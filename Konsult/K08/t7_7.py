def nsd(n,m):
    return 1

def nsk(n, m):
    return n * m // nsd(n, m)


# nsk(a1, a2, a3, .... an) =
#     nsk(nsk(nsk(a1, a2), a3), ..., an))

n = int(input())
res = 1
for i in range(2, n + 1):
    res = nsk(res, i)
