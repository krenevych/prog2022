from Triangle import *
from random import randint
from turtle import *

colors = [
    "green",
    "firebrick",
    "dark magenta",
    "spring green",
    "floral white",
    "medium blue",
    "dodger blue"
]

def buildTriangles(n, rangeCoords, colorList):
    triangles = []

    for i in range(n):
        x1 = randint(rangeCoords[0], rangeCoords[1])
        y1 = randint(rangeCoords[0], rangeCoords[1])
        x2 = randint(rangeCoords[0], rangeCoords[1])
        y2 = randint(rangeCoords[0], rangeCoords[1])
        x3 = randint(rangeCoords[0], rangeCoords[1])
        y3 = randint(rangeCoords[0], rangeCoords[1])
        triangle = Triangle(x1, y1, x2, y2, x3, y3)
        triangles.append(triangle)

        colors_num = len(colorList)
        color_index = randint(0, colors_num - 1)
        color = colorList[color_index]
        triangle.setColor(color)

    return triangles


if __name__ == '__main__':
    triangles = buildTriangles(100, (-300, 300), colors)
    reset()

    for triangle in triangles:
        triangle.draw()

    mainloop()
