lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#   -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1
# print(lst[len(lst) - 2])
# print(lst[- 2])

# print(lst[3 : 8 : 2])
# print(lst[3 : 8])    # [3, 4, 5, 6, 7]
# print(lst[3:]) # [3, 4, 5, 6, 7, 8, 9, 10]
# print(lst[:7])  # [0, 1, 2, 3, 4, 5, 6]
# print(lst[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst[-4 : -2]) # з четвертого (рахуючи з 1) елемента з кінця по другий елемент з кінця
# print(lst[-2: -7 : -1]) # [9, 8, 7, 6, 5]
# print(lst[1:-1]) # список без першого і останнього
print(lst[ : :-1]) # реверс списку