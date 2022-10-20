N = int(input())

a = []  # створюється порожній список
for j in range(N):
    el = int(input())
    a.append(el)  # додавання елементу в масив

# print(*a[::-1])
# 3 4 5 6 8
# 0 1 2 3 4

for i in range(N // 2):  # цикл
    # a[i] <-> a[N - 1 - i]
    tmp = a[i]
    a[i] = a[N - 1 - i]
    a[N - 1 - i] = tmp
    pass

print(*a)
