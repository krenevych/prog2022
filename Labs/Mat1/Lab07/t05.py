# 0 1 10 11 100 101 110 111 1000 1001

# Variant 1
#  101
#  100  ДОДАВАННЯ У СТОВПЧИК
# 1001

# Variant 2 will be implemented here
#  101 -> 5
#  100 -> 4
# 5 + 4 = 9 -> 1001

# 1011(10) = 1*10**3 + 0*10**2 + 1*10**1 + 1*10**0

# 1011(2) = 1*2**3 + 0*2**2 + 1*2**1 + 1*2**0
#      =  8 + 0 + 2 + 1 = 11

def BinToDec(b):
    pow2 = 1
    d = 0
    while b > 0:
        r = b % 10
        d += r * pow2
        b = b // 10
        pow2 *= 2
    return d

def BinToDec2(b : str):
    d = 0
    for c in b:
        r = int(c)
        d = d * 2 + r
    return d

# 29(10) -> ???(2)
# 1 2 4 8 16 32 64
# 29 : 16 8  4 2 1
#      29 13 5 1 1
# 11101

def DecToBin2(d):
    pow10 = 1
    b = 0
    while d > 0:
        r = d % 2
        b += r * pow10
        d = d // 2
        pow10 *= 10
    return b
# 29 14 7
def DecToBin(d):
    if d == 0:
        return "0"

    b = ""
    while d > 0:
        r = d % 2
        b = str(r) + b
        d = d // 2
    return b

def main():
    A = int(input())  # A = 101
    B = int(input())  # B = 100
    Adec = BinToDec(A)  # Adec = 5
    Bdec = BinToDec(B)  # Bdec = 4
    Cdec = Adec + Bdec  # Cdec = 9
    C = DecToBin(Cdec)  # C = 1001
    print(C)

########## Main ##############
main()
# d = BinToDec2("11101")
# print(d)
# b = DecToBin(29)
# print(b)