# n = 12345

n = int(input())

counter = 0 if n > 0 else 1

while n > 0:
    n = n // 10
    counter += 1

print(counter)

