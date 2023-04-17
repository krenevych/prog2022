import math

# x = math.pi / 4
x = float(input("x = "))
eps = 0.00001

a = x
y = x
n = 0

while abs(a) >= eps:
    n += 1
    a *= -x**2 / (2 * n * (2 * n + 1))
    y += a

print(math.sin(x))
print(y, n)

