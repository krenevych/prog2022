def min2(a, b):
    return a if a <= b else b

def min(a, b, c):
    return min2(a, min2(b, c))

def max(a, b):
    return a if a >= b else b

##### Main program #######
x, y, z = [float(el) for el in input().split()]
res = min(max(x, y), max(y, z), x + y + z)
print("%0.2f" % res)
