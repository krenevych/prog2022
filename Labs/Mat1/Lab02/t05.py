a, b, c = [int(el) for el in input().split()]

condition1 = a ** 2 + b ** 2 == c ** 2
condition2 = a ** 2 + c ** 2 == b ** 2
condition3 = c ** 2 + b ** 2 == a ** 2

if condition1 or condition2 or condition3:
    print("YES")
else:
    print("NO")