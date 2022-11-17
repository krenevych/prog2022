# f g
#         f g
# 1 1 2 3 5 8 13

def fib1(n):
    # не рекурсивний варіант
    f, g = 1, 1
    for i in range(3, n + 1):
        f, g = g, f + g
    return g

def fib(n):
    # рекурсивний варіант
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

fibs = [0, 1, 1] # глобальна змінна

def fib_optimize(n):
    global fibs
    # оптимізований рекурсивний варіант, кешує знайдені числа Фібоначчі
    if n < len(fibs):
        return fibs[n]

    f = fib_optimize(n - 1) + fib_optimize(n - 2)
    fibs.append(f)
    return f

# print(fib(37)) # 24157817
# print(fib_optimize(137))
# print(fib_optimize(107))
N = int(input())
for i in range(N):
    n = int(input())
    print(fib1(n))