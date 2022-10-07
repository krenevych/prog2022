# n = 12345
n = int(input())
# 4 6 5 9: ((4 * 10 + 6) * 10 + 5) * 10 + 5

inv = 0
while n > 0:
    last = n % 10
    inv = inv * 10 + last

    # print(last)
    n = n // 10

print(inv)

