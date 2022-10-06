n = int(input()) # n = 7 -> 2 4
# n = 33 -> m = 2 4 8 16 32

m = 2
while m < n:
    print(m, end=' ')
    m = m * 2