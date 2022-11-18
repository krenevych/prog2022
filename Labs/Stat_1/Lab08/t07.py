

def divide(n, prev, lst : list):
    if n == 0:
        print(*lst)
    else:
        for i in range(prev, n+1):
            newlst = lst[:]

            newlst.insert(0, i)
            divide(n - i, i, newlst)


n = int(input())
divide(n, 1, [])

