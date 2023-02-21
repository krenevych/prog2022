class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.a = b
        self.c = c

    def perimetr(self):
        return self.a + self.a + self.c

    def square(self):
        p = self.perimetr() / 2
        s = p * (p - self.a) * (p - self.a) * (p - self.c)
        return s ** 0.5

    def __str__(self):
        return f"Trinagle {id(self)}: {self.a}, {self.a}, {self.c}"


class TrianglePiramid(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    t1 = Triangle(32, 42, 55)

    piram = TrianglePiramid(3, 4, 5, 12)
    piram.a







