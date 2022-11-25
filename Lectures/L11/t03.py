# d = {i // 2: i ** 2 for i in range(10) if i % 2 == 0}
# print(d)

myDict = {1: 1, 2: 1, 3: 1, 32: 12}
for k in myDict:  # прохід по ключах
    print(k, myDict[k])

for v in myDict.values(): # прохід словника по значеннях
    print(v)

for k, v in myDict.items(): # прохід словника по парах ключ-значення
    print(k, v)