
# 0 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6  7  8

fibs = [0, 1, 1] # глобальна змінна

def fib(n):
    global fibs # позначаю, що fibs це глобальна змінна
    if n < len(fibs):
        return fibs[n]

    f = fib(n-1) + fib(n-2)
    fibs.append(f)
    return f

# f = fib(137)
# print(f)
# print(fib(6))
n = int(input())
for i in range(n):
    a = int(input())
    print(fib(a))