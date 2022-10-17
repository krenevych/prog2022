# Задано N та послідовність a1, a2, ... aN.
# Знайти найбільше серед заданих чисел
# 10; 1 7 23 15 3 12 9 34 13 6 -> max

N = int(input("N = "))

maximum = int(input("a = "))
for i in range(1, N):
    a = int(input("a = "))
    if a > maximum:
        maximum = a

print("Max = ", maximum)

