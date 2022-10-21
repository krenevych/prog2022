N = int(input())

lst = [int(el) for el in input().split()]

mx = lst[0]

for item in lst:
    if item > mx:
        mx = item

print(mx)