# Задано три дійсні числа х, у та z. Обчислити
# min (max(x,y),max(y,z),x+y+z),
# скориставшись допоміжними функціями для обчислення мінімального та максимального
# значення з двох елементів

def min2(a, b):
    return a if a < b else b

def min3(a, b, c):
    return min2(min(a, b), c)

def max2(a, b):
    return a if a > b else b

####### Main #############
x, y, z = [float(el) for el in input().split()]
res = min3(max2(x,y),max2(y,z),x+y+z)
print("%.2f" % res)