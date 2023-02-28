from Equation import Equation


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self._a = a

    def discriminant(self):
        return self._b ** 2 - 4 * self._a * self._c

    def solve(self):
        if self._a == 0:  # це означає, що в нас лінійне рівняння
            return super().solve()
        else:  # точно квадратне рівняння
            d = self.discriminant()
            if d < 0:  # розв'язків немає
                return ()
            elif d == 0:  # один розв'язок
                return -self._b / (2 * self._a),
            else:  # d > 0, два розв'язки
                d_2 = d ** 0.5
                x1 = (-self._b - d_2) / (2 * self._a)
                x2 = (-self._b + d_2) / (2 * self._a)
                return x1, x2

    def __str__(self):
        if self._a == 0:
            return super().__str__()

        return f"{id(self)}: {self._a} x**2 + {self._b}x + {self._c} = 0"


if __name__ == '__main__':
    q_eq = QuadraticEquation(1, 3, 2)
    q_eq.show()
    print(q_eq.solve())
