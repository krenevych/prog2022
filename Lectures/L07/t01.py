# Опишемо функцію, що повертає більше з двох значень.

def max2(a, b):
    if a > b:
        return a
    else:
        return b

# c = max2(6, 7)
# print(c)

# max(1, 5, 3)
print(max2(1, max2(5, 3)))