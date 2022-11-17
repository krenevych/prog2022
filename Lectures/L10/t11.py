import math


def table(points, func, title="func"):
    for x in points:
        print(f"{title}({x})={func(x)}")


myfunc = lambda x: x ** 2
print(myfunc(4))

# table([0, 0.1, 0.2, 0.3], lambda x: x ** 3)

