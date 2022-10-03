x, y =  [float(el) for el in input().split()]

cond = x ** 2 + y ** 2 < 4 and x < 0 or abs(x) + abs(y) < 2 and x >= 0

print("Точка (%f, %f) належить до заданої області:" %(x, y), cond )