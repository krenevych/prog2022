n, m = [int(el) for el in input().split()]

# for i in range(1, n * m + 1):
#     print(i, end=" ")
#     if i % m == 0:
#         print()

M = []
for i in range(n):
    row = []
    M.append(row)
    for j in range(m):
        row.append(m * i + j + 1)

print(M)