def mult(n, m):
    if m == 0:
        return 0
    else:
        # рекурсивний виклик
        return mult(n, m - 1) + n


# mult(n, 0) = 0
# mult(n, m) = mult(n, m - 1) + n


# n * m = (n + n + n + ... + n) + n
#         ----- m -1 --------

f = mult(4, 3)

