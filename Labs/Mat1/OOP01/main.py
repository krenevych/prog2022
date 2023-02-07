from QuadraticEquation import QuadraticEquation


def readQuadraticEquation(file):
    equations = []
    with open(file) as f:
        for line in f:
            try:
                coefs = [float(coef) for coef in line.split() ]
                assert len(coefs) == 3
                eq = QuadraticEquation(*coefs)
                equations.append(eq)
            except AssertionError:
                continue

    return equations


if __name__ == '__main__':
    equations = readQuadraticEquation("input01.txt")
    for equation in equations:
        print(f"solution of equation {equation} is {equation.solutions()}")
