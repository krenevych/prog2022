def fact(n):
    if n == 0:
        # 0! = 1
        return 1
    else:
        # 5! = 4! * 5
        prev = fact(n - 1)
        return prev * n

f = fact(5)


