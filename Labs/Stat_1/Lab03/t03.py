# 4! = 1 * 1 * 2 * 3 * 4
# 0! = 1
# 1! = 0! * 1 = 1
# 2! = 1! * 2 = 2
# 3! = 2! * 3 = 6
# 4! = 3! * 4 = 24

n = int(input())

f = 1
k = 0
while k < n:
    k += 1
    f *= k

print(f)