N = int(input("N = "))

# N - просте, якщо воно ділиться лише на 1 та на N

n = 2
is_prime = True
while n < N:
    res = N % n
    if res == 0:
        is_prime = False
    n += 1

print("число %d є простим це " % N, is_prime)