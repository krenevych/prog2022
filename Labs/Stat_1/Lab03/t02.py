# n = 33 => 2 4 8 16 32

n = int(input())
pow2 = 2
while pow2 < n:
    print(pow2, end=" ")
    pow2 *= 2

