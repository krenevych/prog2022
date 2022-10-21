n = int(input())

lst = [0] * 10 # lst = [0,0,0,0,0,0,0,0,0,0]

while n > 0:
    d = n % 10
    lst[d] += 1
    n = n // 10

print(*lst)

