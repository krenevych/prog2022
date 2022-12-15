#      0   1    2
# [
#0:   [4, -2,   5],
#1:   [1, -4, -12],
#2:   [0,  1,  -3],
# ]

# M = [
#     [4, -2, 5],
#     [1, -4, -12],
#     [0, 1, -3],
# ]
#
# print(M[1][0])

def readMatrix(n, elements_type=int):
    M = []
    for i in range(n):
        row = [elements_type(el) for el in input().split()]
        M.append(row)
    return M

def writeMatrix(M, pattern="%5d"):
    for row in M:
        for a in row:
            print(pattern % a, end="")
        print()

########### main ##############
########### main ##############
########### main ##############
n = int(input())
M = readMatrix(n)
# writeMatrix(M, "%8.2f")

# len(M) - кількість елементів у списку M,
# тобто кількість рядків нашої матриці

sum_neg = 0
count_neg = 0
for i in range(len(M)): # цикл по рядках
    for j in range(len(M[0])): # цикл по елементам рядка
        # print(M[i][j])
        if M[i][j] < 0 and M[i][j] % 2 == 0:
            sum_neg += M[i][j]
            count_neg += 1

print(count_neg, sum_neg)