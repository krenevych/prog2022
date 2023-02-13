class Triangle:
    def __init__(self, a, b=None, c=None):

        if isinstance(a, Triangle):
            self.isPrimary = False
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            assert a + b > c and a + c > b and b + c > a
            self.isPrimary = True
            self.a = a
            self.b = b
            self.c = c

    def __str__(self):
        return f"Trinagle {id(self)}: {self.a}, {self.b}, {self.c}"


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    t1 = Triangle(t)
    print(t)
    print(t1)

    pass



