# x = int(input("Введіть ціле число"))
# print(x)


try:
    lst = [1, 2, 3]
    print(lst[10])

    myDict = {"one": 1, "two": 2}
    print(myDict["three"])
# except IndexError as e:
#     print("Такого елементу не існує:", e)
# except KeyError as e:
#     print("Такого елементу не існує:", e)
except LookupError as e:
    print("Такого елементу не існує", e, type(e))
