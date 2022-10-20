N = int(input())
lst = [float(x) for x in input().split()]

summ = 0
k = 0
for x in lst[2:N:3]:
    if x > 0:
        summ += x
        k += 1
print(f"{k} {summ:.2f}")