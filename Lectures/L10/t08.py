x = 1

def func():
    global x # вказує функції використовувати глобальну змінну x, а не створювати локальну змінну
    x = 3
    print("x (local) = ", x)

func()

print("x (global) = ", x)