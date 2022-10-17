# Знайти суму чисел від 1 до N
# (N + 1)N / 2

N = int(input("N = "))
suma = (N + 1) * N / 2
# suma = 0
# for i in range(1, N+1): # N, якщо парне також увійде до розрахунку
#     print(i)
    # suma += i

print("suma = ", suma)