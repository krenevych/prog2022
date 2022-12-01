#      0   1    2
#     [4, -2,   5],  0
#     [1, -4, -12],  1
#     [0,  1,  -3],  2

# M[i][j] - на побічній діагоналі,
#           якщо i + j = n - 1 (бо нумерація з нуля)
# M[i][j] - над побічною діагоналлю,
#           якщо i + j < n - 1
# M[i][j] - під побічною діагоналлю,
#           якщо i + j > n - 1

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i + j == n - 1:
#             print(0, end="")
#         elif i + j < n - 1:
#             print(2, end="")
#         else:
#             print(1, end="")
#     print()

n = int(input())
M = []

# створюємо матрицю заповнену нулями
for i in range(n):
    row = [0] * n
    M.append(row)

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            # print(0, end="")
            M[i][j] = 0
        elif i + j < n - 1:
            # print(2, end="")
            M[i][j] = 2
        else:
            # print(1, end="")
            M[i][j] = 1
    # print()

for row in M:
    print(*row, sep="")
