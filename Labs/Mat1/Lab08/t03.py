#                1             0
#              1   1           1
#            1   2   1         2
#          1   3   3   1       3
#        1   4   6   4   1     4
#      1   5   10  10  5   1   5

# C(n, k)
# C(n, 0) = 1, C(n, n) = 1
# C(5, 2) = C(4, 1) + C(4, 2)
# C(3, 1) = C(2, 0) + C(2, 1)
# C(n, k) = C(n-1, k-1) + C(n-1, k)

def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k-1) + C(n-1, k)

############# Main ##############
print(C(5, 2))