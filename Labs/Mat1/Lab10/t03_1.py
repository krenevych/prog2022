def printM(M):
    for row in M:
        print(*row, sep="")

#     0 1 2
# 0 : 2 2 0
# 1 : 2 0 1
# 2 : 0 1 1

n = int(input())
M = []
for i in range(n):
    row = [0] * n
    M.append(row)

# M = [[0] * n] * n
printM(M)
M[0][1] = 1
print()
printM(M)

# for i in range(n):  # пробігаємо по індексах рядків
#     for j in range(n):  # пробігаємо по індексах стовпчиків
#         # i == j - на головній діагоналі
#         # i + j == n - 1 - на побічній діагоналі
#         # i + j < n - 1 - вище побічної діагоналі
#         # i + j > n - 1 - нижче побічної діагоналі
#         if i + j == n - 1:
#             M[i][j] = 0
#         elif i + j < n - 1:
#             M[i][j] = 2
#         else:
#             M[i][j] = 1
#
# for row in M:
#     print(*row, sep="")