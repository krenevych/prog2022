# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 112233888888

n = int(input())
a = [0] * 10  # a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while n > 0:
    last = n % 10
    a[last] += 1
    n = n // 10

print(*a)