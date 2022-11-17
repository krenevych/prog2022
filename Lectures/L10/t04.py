def suma(*args):
    res = 0
    for el in args:
        res += el
    return res
    # print(args)
    # return a1 + a2 + a3



a = suma(1, 2, 3, 5, 6, 7)
print(a)
