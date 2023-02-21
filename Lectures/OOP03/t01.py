class Triangle:

    numberOfSide = 3  # статичне поле

    @staticmethod   # статичний метод
    def getNumberOfSides():
        Triangle.numberOfSide += 1

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


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    t1 = Triangle(32, 42, 55)

    t.getNumberOfSides()

    print(Triangle.numberOfSide)
    print(t.numberOfSide)
    print(t1.numberOfSide)





