a, b, x, y, z = [float(el) for el in input().split()]

if x < a and y < b:
    print(1)
elif y < a and x < b:
    print(1)

elif z < a and y < b:
    print(1)
elif y < a and z < b:
    print(1)

elif z < a and x < b:
    print(1)
elif x < a and z < b:
    print(1)
else:
    print(0)