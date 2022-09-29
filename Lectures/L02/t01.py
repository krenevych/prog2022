x = int(input("Введіть число "))

# abs_x = 0
if x < 0:
    abs_x = -x
else:
    abs_x = x

print("Модуль числа |%d| = %d" % (x, abs_x))