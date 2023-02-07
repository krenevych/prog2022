class QuadraticEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print(f"{self.a} x**2 + {self.b}x + {self.c} = 0")

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solutions(self):
        if self.a == 0:  # рівняння вироджується в лінійне
            if self.b != 0:  # bx + c = 0
                return -self.c / self.b,  # кортеж з одного елементу
            else:  # c = 0
                if self.c == 0:  # 0 = 0
                    return "Inf"  # стала "Inf" означає, що в нас нескінченна кількість розв'язків
                else:  # 3 = 0
                    return ()  # розв'язків немає
        else:            # повноцінне квадратне рівняння
            d = self.discriminant()
            if d < 0:  # розв'язків немає
                return ()
            elif d == 0:                         # один розв'язок
                return -self.b / (2 * self.a),
            else:                                # d > 0, два розв'язки
                d_2 = d ** 0.5
                x1 = (-self.b - d_2) / (2 * self.a)
                x2 = (-self.b + d_2) / (2 * self.a)
                return x1, x2


############## - MAIN - ########################
eq1 = QuadraticEquation(1, 4, 14)
eq1.show()
print("solutions = ", eq1.solutions())

eq2 = QuadraticEquation(1, 4, 4)
eq2.show()
print("solutions = ", eq2.solutions())

eq3 = QuadraticEquation(1, -3, 2)
eq3.show()
print("solutions = ", eq3.solutions())

lin_eq1 = QuadraticEquation(0, -3, 2)
lin_eq1.show()
print("solutions = ", lin_eq1.solutions())

lin_eq2 = QuadraticEquation(0, 0, 2)
lin_eq2.show()
print("solutions = ", lin_eq2.solutions())

lin_eq3 = QuadraticEquation(0, 0, 0)
lin_eq3.show()
print("solutions = ", lin_eq3.solutions())
