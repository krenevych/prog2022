# Задано послідовність a1, a2, ... aN, 0.
# Знайти найбільше додатне серед заданих чисел
# 1 7 -23 15 -3 12 9 -34 13 6, 0 -> max

maximum = 0  # бо всі додатні числа більші нуля.
while True:
    a = int(input("a = "))
    if a == 0:
        break
    if a < 0:
        continue
    if a > maximum:
        maximum = a


print("Max = ", maximum)

