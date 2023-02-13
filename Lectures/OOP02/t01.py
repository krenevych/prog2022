from copy import copy

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

    def __str__(self):
        return f"Trinagle {id(self)}: {self.a}, {self.b}, {self.c}"

    ########### MAIN ###############


t = Triangle(3, 4, 5)
t1 = copy(t)
print(t)
print(t1)
t1.a = 12
print(t)
print(t1)


