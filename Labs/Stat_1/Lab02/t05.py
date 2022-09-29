a, b, c = [int(el) for el in input().split()]

c1 = a ** 2 + b ** 2 == c ** 2
c2 = a ** 2 + c ** 2 == b ** 2
c3 = c ** 2 + b ** 2 == a ** 2

if c1 or c2 or c3:
    print("YES")
else:
    print("NO")
