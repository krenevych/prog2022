# N = int(input())
# a = [float(el) for el in input().split()]
#
# for i in range(N):
#     j = i + 1
#     print(j, " : " , a[i])

N = int(input())
a = [float(el) for el in input().split()]

sum = 0
counter = 0
for i in range(2, N, 3):
    # print(a[i])
    if a[i] > 0:
        counter += 1
        sum += a[i]

print(counter, "%0.2f" % sum, sep=' ')