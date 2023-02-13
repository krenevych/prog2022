class Triangle:
    def __init__(self, a, b=None, c=None):

        if isinstance(a, Triangle):
            self._a = a._a
            self._b = a._b
            self._c = a._c
        else:
            assert a + b > c and a + c > b and b + c > a
            self._a = a
            self._b = b
            self._c = c

    def set_a(self, a):
        assert a + self._b > self._c and a + self._c > self._b and self._b + self._c > a
        self._a = a

    def set_b(self, b):
        assert self._a + b > self._c and self._a + self._c > b and b + self._c > self._a
        self._b = b

    def set_c(self, c):
        assert self._a + self._b > c and self._a + c > self._b and self._b + c > self._a
        self._c = c

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def perimetr(self):
        return self._a + self._b + self._c

    def square(self):
        p = self.perimetr() / 2
        s = p * (p - self._a) * (p - self._b) * (p - self._c)
        return s ** 0.5

    def __str__(self):
        return f"Trinagle {id(self)}: {self._a}, {self._b}, {self._c}"


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    print(t.get_c())
    t._c = 123456

    print(t.square())
