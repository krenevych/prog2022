class QuadraticEquation:

    def __init__(self, a, b=None, c=None):
        if isinstance(a, QuadraticEquation): # a - це квадратне рівняння, тобто екземпляр класу QuadraticEquation
            self.__a = a.__a
            self.__b = a.__b
            self.__c = a.__c
        else:
            self.__a = a
            self.__b = b
            self.__c = c

    def clone(self):
        return QuadraticEquation(self.__a, self.__b, self.__c)

    def show(self):
        print(self)

    def __str__(self):
        return f"{id(self)}: {self.__a} x**2 + {self.__b}x + {self.__c} = 0"

    def discriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def solutions(self):
        if self.__a == 0:  # рівняння вироджується в лінійне
            if self.__b != 0:  # bx + c = 0
                return -self.__c / self.__b,  # кортеж з одного елементу
            else:  # c = 0
                if self.__c == 0:  # 0 = 0
                    return "Inf"  # стала "Inf" означає, що в нас нескінченна кількість розв'язків
                else:  # 3 = 0
                    return ()  # розв'язків немає
        else:            # повноцінне квадратне рівняння
            d = self.discriminant()
            if d < 0:  # розв'язків немає
                return ()
            elif d == 0:                         # один розв'язок
                return -self.__b / (2 * self.__a),
            else:                                # d > 0, два розв'язки
                d_2 = d ** 0.5
                x1 = (-self.__b - d_2) / (2 * self.__a)
                x2 = (-self.__b + d_2) / (2 * self.__a)
                return x1, x2


if __name__ == '__main__':
    eq1 = QuadraticEquation(1, 4, 14)
    print(eq1)
    print("solutions = ", eq1.solutions())

    copy_eq1 = QuadraticEquation(eq1)
    # copy_eq1 = eq1.clone()
    copy_eq1._QuadraticEquation__a = 0
    print(copy_eq1)
    print("solutions = ", copy_eq1.solutions())

