class Equation:

    INF = "Inf"

    """
    Клас Лінійне алгебраїчне рівняння bx + c = 0.
    """
    def __init__(self, b, c):
        self._b = b
        self._c = c

    def solve(self):
        # b != 0 => x = -c / b
        if self._b != 0:
            return -self._c / self._b,
        # b = 0:
        elif self._c == 0:  # c = 0 => 0 = 0 => inf
            return Equation.INF
        else:  # c != 0 => 3 = 0 => розв'язків немає
            return ()

    def show(self):
        print(self)

    def __str__(self):
        return f"{id(self)}: {self._b}x + {self._c} = 0"


if __name__ == '__main__':
    eq = Equation(0, 0)
    print(eq)
    print(eq.solve())

