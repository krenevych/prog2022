class Triangle:

    def __init__(self, a, b, c):
        assert a + b > c and a + c > b and b + c > a

        self.a = a
        self.b = b
        self.c = c

    def __del__(self):
        print("Object deleted", self)

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return s ** 0.5

    ########### MAIN ###############


t1 = Triangle(3, 4, 5)
print("Трикутник зі сторонами ", t1.a, t1.b, t1.c)
print("Square", t1.square())
#
# t2 = Triangle(5, 6, 7)
# print("Perimetr", t2.perimetr())
# print("Square", t2.square())
