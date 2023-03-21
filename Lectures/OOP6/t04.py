# n: 0   1   2   3   4   5   6   7
#       Fn2
#           Fn1
# F: 1   1   2   3   5   8   13  21
#            F
Fn_2 = 1   # F0 = 1
Fn_1 = 1   # F1 = 1

N = 6

for n in range(2, N+1):
    F = Fn_1 + Fn_2
    Fn_2 = Fn_1
    Fn_1 = F


print(Fn_1)


