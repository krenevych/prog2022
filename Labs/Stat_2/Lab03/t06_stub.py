# n = 12345 => 54321

# n = 12345
n = int(input())
while n > 0:
    last = n % 10
    print(last, end="")
    # print(last)
    n = n // 10