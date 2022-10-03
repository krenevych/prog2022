a, b, c = [int(el) for el in input().split()]


cond2 = (a ** 2 + b ** 2 + c ** 2
         == 2 * max(a, b, c) ** 2)

if cond2:
    print("YES")
else:
    print("NO")
