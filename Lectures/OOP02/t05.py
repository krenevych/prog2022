class Triangle:
    def __init__(self, a, b=None, c=None):

        if isinstance(a, Triangle):
            self.__a = a.__a
            self.__b = a.__b
            self.__c = a.__c
        else:
            assert a + b > c and a + c > b and b + c > a
            self.__a = a
            self.__b = b
            self.__c = c

    def set_a(self, a):
        assert a + self.__b > self.__c and a + self.__c > self.__b and self.__b + self.__c > a
        self.__a = a

    def set_b(self, b):
        assert self.__a + b > self.__c and self.__a + self.__c > b and b + self.__c > self.__a
        self.__b = b

    def set_c(self, c):
        assert self.__a + self.__b > c and self.__a + c > self.__b and self.__b + c > self.__a
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def perimetr(self):
        return self.__a + self.__b + self.__c

    def square(self):
        p = self.perimetr() / 2
        s = p * (p - self.__a) * (p - self.__b) * (p - self.__c)
        return s ** 0.5

    def __str__(self):
        return f"Trinagle {id(self)}: {self.__a}, {self.__b}, {self.__c}"


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    print(t._Triangle__c) # FIXME: remove this debug code
    t.__c = 1234
    print(t.__c)
    pass




