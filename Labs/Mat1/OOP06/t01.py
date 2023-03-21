class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Vector2D(self.x + other, self.y + other)
        elif isinstance(other, Complex):
            return Vector2D(self.x + other.re, self.y + other.im)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f"{self.re} + {self.im}i"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Complex(self.re + other.x, self.im + other.y)
        elif isinstance(other, float) or isinstance(other, int):
            return Complex(self.re + other, self.im)
        elif isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)


if __name__ == '__main__':
    v1 = Vector2D(1, 1)
    print(v1)
    c = Complex(1, 7)
    print(c)

    c1 = c + 66
    print(c1)

    v4 = v1 + c
    print(v4)

    c4 = c + v1
    print(c4)


