n = int(input())

# 21 : 3, 7
# 9 : 3

# n : p, q

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(n // i)
        break
else:
    print(1)
