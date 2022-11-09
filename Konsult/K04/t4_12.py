i = 0
while True:
    n = int(input())
    if n % 2 != 0:
        continue
    if n % 2 == 0 and n == 0:
        break
    i += n

print(i)

# 123
