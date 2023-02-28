from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    def solve(self):
        solutions = super().solve()
        if solutions == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        solutions_set = set()
        for solution in solutions:
            if solution < 0:
                continue
            else:
                sol = solution**0.5
                solutions_set.add(sol)
                solutions_set.add(-sol)
        return tuple(solutions_set)

    def __str__(self):
        return f"{id(self)}: {self._a} x**4 + {self._b}x**2 + {self._c} = 0"


if __name__ == '__main__':
    b_eq = BiQuadraticEquation(1, 3, 2)
    b_eq.show()
    print(b_eq.solve())

