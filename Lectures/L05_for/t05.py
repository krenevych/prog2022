# Знайти суму парних чисел від 1 до N

N = int(input("N = "))
suma = 0
for i in range(2, N+1, 2): # N, якщо парне також увійде до розрахунку
    print(i)
    suma += i

print("suma = ", suma)