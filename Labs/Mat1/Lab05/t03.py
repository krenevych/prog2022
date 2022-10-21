N = int(input())

lst = [float(el) for el in input().split()]

cnt = 0
sum = 0

for i in range(2, N, 3):
    if lst[i] > 0:
        cnt += 1
        sum += lst[i]

print('%d %.2f' % (cnt, sum))