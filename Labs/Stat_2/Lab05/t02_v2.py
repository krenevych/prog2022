# 4
# 1 2 3 -4

N = int(input())
a = [int(el) for el in input().split()]

# for e in a: # e = поточний елелемент масиву
#     if e >= 0:
#         e += 2
#     print(e, end=" ")

# N = len(a) - вже є як результат зчитування вхідних даних
for i in range(N):
    if a[i] >= 0:
        a[i] += 2

# for e in a:
#     print(e, end=" ")
# print(a) # print([3, 4, 5, -4])
print(*a, sep=" ") # print(3, 4, 5, -4)
