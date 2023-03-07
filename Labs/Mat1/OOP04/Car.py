from Figure import *


class Car(Figure):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

        self.parts = [
            Rectangle(x, y, 200, 50, color),
            Circle(x + 30, y, 30, color),
            Circle(x + 150, y, 30, color),
            Triangle(x + 100, 50, 100, color)
        ]


    def _draw(self, color):
        for element in self.parts:
            element._draw(color)

    def _move(self, dx, dy):
        for element in self.parts:
            element._move(dx, dy)


if __name__ == '__main__':
    car = Car(100, 0, "red")

    car.show()

    car.move(-300, -200)
    car.move(300, 0)

    home()
    mainloop()









