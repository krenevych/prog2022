N = int(input())
lst = [int(x) for x in input().split()]


maximum = lst[0]
for el in lst[1:]:
    if el > maximum:
        maximum = el
print(maximum)

# print(max(lst)) - зразу шукає найбільший елемент масиву
