import math

# x = float(input("Введіть площу кільця "))
# y = float(input("Введіть радіус зовнішнього кола "))

x, y = [float(d) for d in input().split()]

r = (((math.pi * (y ** 2)) - x) / math.pi) ** 0.5


pass
# print("%0.2f" % r)


# print((round(((()))