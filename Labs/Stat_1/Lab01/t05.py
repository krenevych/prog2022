# Задано дійсні числа x1, y1, x2, y2, x3, y3, значення
# яких відповідають координатам вершин трикутника.
# Визначити периметр та площу трикутника.
# 3 2 7 6.5 10 1

x1, y1, x2, y2, x3, y3 = [float(d) for d in input().split()]

a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5

perimetr = a + b + c
p = perimetr / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("%0.4f %0.4f" % (perimetr, s))