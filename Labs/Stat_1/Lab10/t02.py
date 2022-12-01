n, m = [int(el) for el in input().split()]

# M = []
# for i in range(1, n * m + 1):
#     M.append(i)
#     # print(i, end=" ")
#     # if i % m == 0:
#     #     print()
#
# print(M)

M = []
# current = 1
for i in range(n):
    row = []
    M.append(row)
    for j in range(m):
        row.append(i * m + j + 1)
        # current += 1

print(M)

