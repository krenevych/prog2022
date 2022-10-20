N = int(input())
lst = [int(input()) for x in range(N)]

for i in range(N // 2):
    lst[i], lst[N-1-i] = lst[N-1-i], lst[i]

print(*lst)

# print(*lst[::-1])
