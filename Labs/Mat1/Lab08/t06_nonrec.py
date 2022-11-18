#               g f
# 1 1 2 3 5 8 13 21
# 1 2 3 4 5 6  7  8

def fib(n):
    g, f = 1, 1
    for i in range(3, n+1):
        g, f = f, g + f

    return f

n = int(input())
for i in range(n):
    a = int(input())
    print(fib(a))