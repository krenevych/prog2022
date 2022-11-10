def BinToDec(b):
    # b = 101 -> 5
    # 1101 = 1 * 2**0 + 0 * 2 ** 1 + 1 * 2 **2 + 1 * 2 ** 3
    dec = 0   # число в десятковій системі
    pow2 = 1  # розряди двійкової системи числення, тобто 2**k
    while b > 0:
        r = b % 10 # цифра при відповідному розряді
        dec += r * pow2
        b = b // 10
        pow2 *= 2

    return dec

# 29(10) -> ????(2)
# 1  2  4  8  16  32  64
# 16  8  4  2  1
# 11101
# 13, 5, 1

# 29, 14  7  3  1  0
# 1   0   1  1  1

def DecToBin(d):
    if d == 0:
        return "0"

    # d = 4 -> 100
    bin = ""   # число в двійковій системі
    while d > 0:
        r = str(d % 2) # цифра при відповідному розряді
        bin = r + bin
        d = d // 2

    return bin

def main():
    A = int(input())  # подається у двійковій
    B = int(input())  # подається у двійковій

    a_dec = BinToDec(A)  # A = 101, a_dec = 5
    b_dec = BinToDec(B)  # B = 100, b_dec = 4
    c_dec = a_dec + b_dec  # c_dec = 9
    C = DecToBin(c_dec)  # C = 1010
    print(C)

######### Main ##############
main()
# print(BinToDec(11101))
# print("'",DecToBin(0), "'", sep="")



