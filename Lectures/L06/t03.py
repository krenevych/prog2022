lst = [1, 2, 3, 4, 5]
#      0  1  2  3  4
print(lst)
# lst[len(lst):len(lst)] = [6]  # lst.append(6)
lst[2:2] = [555, 666, 7777]  # lst.insert(2, [555, 666, 7777])
print(lst)
lst[2:5] = [] # видалення з 2 до 4й елементи
print(lst)
