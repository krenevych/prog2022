N = int(input())

lst = [int(el) for el in input().split()]

for i in range(0, N):
    if lst[i] >= 0:
        lst[i] += 2

print(*lst)