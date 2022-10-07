# 4! = 1 * 1 * 2 * 3 * 4
# 0! =                  1
# 1! = 0! * 1 = 1 * 1 = 1
# 2! = 1! * 2 = 1 * 2 = 2
# 3! = 2! * 3 = 2 * 3 = 6
# 4! = 3! * 4 = 6 * 4 = 24

n = int(input())
k = 0
factorial = 1

while k < n:
    k += 1
    factorial *= k

print(factorial)
