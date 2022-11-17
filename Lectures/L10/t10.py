import math

def table(points, func, title="func"):
    for x in points:
        print(f"{title}({x})={func(x)}")

table([0, math.pi/6, math.pi/4,math.pi/3, math.pi/2], math.sin, "sin")