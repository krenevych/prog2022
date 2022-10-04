x3, y3 = [int(d) for d in input().split()] # C
x1, y1 = [int(d) for d in input().split()] # A
x2, y2 = [int(d) for d in input().split()] # B

cond1 = (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1) # умова того, що на одній прямій
AC2 = (x3 - x1) ** 2 + (y3 - y1) ** 2
BC2 = (x3 - x2) ** 2 + (y3 - y2) ** 2
AB2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
AC = AC2 ** 0.5
BC = BC2 ** 0.5
AB = AB2 ** 0.5




if cond1: # перевірка, що лежить на прямій
    print("YES") # лежить на прямій

    x_AC = x3 - x1
    y_AC = y3 - y1

    x_AB = x2 - x1
    y_AB = y2 - y1

    dot_AC_AB = x_AC * x_AB + y_AC * y_AB

    if dot_AC_AB >= 0:    # перевірка, що на промені
        print("YES")
    else:
        print("NO")

    if AC + BC == AB: # або відрізку
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    print("NO")
    print("NO")

