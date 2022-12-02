#  [
#    0    1    2
#   [4,  -2,   5],   # 0
#   [1,  -4, -12],   # 1
#   [0,   1,  -3],   # 2
# ]

n = int(input())
M = []
for i in range(n):
    row = [int(a) for a in input().split()]
    # print(row)
    M.append(row)

# print(M)

# for row in M:  # пробігаємо по кожному рядку
#     for a in row:  # пробігаємо по всіх елементах рядка
#         print("%5d" % a, end="")
#     print()

counter = 0
suma = 0
# for row in M: # пробігаємо по кожному рядку
#     for a in row:  # пробігаємо по всіх елементах рядка
#         if a < 0 and a % 2 == 0:
#             counter += 1
#             suma += a

# len(M) -  кількість рядків матриці M
# len(M[0]) - кількість стовпчиків у матриці M

for i in range(len(M)): # пробігаємо по номерах рядків матриці
    for j in range(len(M[0])): # пробігаємо по номерах стовпчиків матриці
        if M[i][j] < 0 and M[i][j] % 2 == 0:
            counter += 1
            suma += M[i][j]


print(counter, suma)

