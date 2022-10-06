# n = 12345 => 54321

n = 12345
# n = int(input())

inv = 0
while n > 0:
    last = n % 10
    inv = inv * 10 + last
    n = n // 10

print(inv)