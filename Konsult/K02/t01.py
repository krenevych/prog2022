a, b, c = [int(d) for d in input().split()]
if a == b and b == c:
    print(1)
elif a != b and b != c and a != c:
    print(3)
else:
    print(2)

