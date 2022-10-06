n = int(input())

count = 0 if n > 0 else 1
while n > 0:
    n = n // 10
    count += 1
    pass

print(count)


