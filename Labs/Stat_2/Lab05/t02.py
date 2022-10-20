# 4
# 1 2 3 -4

N = int(input())
a = [int(el) for el in input().split()]

for e in a:
    if e >= 0:
        print(e + 2, end=" ")
    else:
        print(e, end=" ")

