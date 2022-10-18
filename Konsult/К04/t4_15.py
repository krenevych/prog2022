# 1: 1, 2, 3, 4, 5, 6, 7, 8, 9
# 10, 99: 11, 13, 15, 17...

# n = int(input())
# n = 2
# start = 10**(n - 1)
# end = 10 ** n
# counter = 0
# for i in range(start, end):
#     tmp_i = i
#     while tmp_i > 0:
#         last = tmp_i % 10
#         if last % 2 == 0:
#             break
#         tmp_i = tmp_i // 10
#     else:
#         counter += 1
#
# print(counter)

n = int(input())
print(5 ** n)