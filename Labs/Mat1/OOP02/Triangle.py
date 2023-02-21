import turtle


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.color = "dark violet"

    def setColor(self, color):
        self.color = color

    def draw(self):
        turtle.up()
        turtle.color(self.color)
        turtle.setpos(self.x1, self.y1)
        turtle.down()
        turtle.setpos(self.x2, self.y2)
        turtle.setpos(self.x3, self.y3)
        turtle.setpos(self.x1, self.y1)
        turtle.up()


if __name__ == '__main__':
    turtle.reset()

    t = Triangle(0, 0, 0, 100, 50, 100)
    t.draw()

    t2 = Triangle(-500, -100, 0, 0, 500, -100)
    t2.setColor("#008000")
    t2.draw()

    turtle.mainloop()  # Затримуємо вікно на екрані
