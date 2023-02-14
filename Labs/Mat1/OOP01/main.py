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

    # Для заданого набору квадратних рівнянь, покажіть ті з них, що:
equations_with_0_solutions = []    # •	не мають розв’язків;
equations_with_1_solutions = []    # •	мають один розв’язок;
equations_with_2_solutions = []    # •	мають два розв’язки;
equations_with_Inf_solutions = []    # •	мають нескінченну кількість розв’язків.


if __name__ == '__main__':
    equations = readQuadraticEquation("input01.txt")
    for equation in equations:
        solutions = equation.solutions()
        if solutions == "Inf":
            equations_with_Inf_solutions.append(equation)
        elif len(solutions) == 0:
            equations_with_0_solutions.append(equation)
        elif len(solutions) == 1:
            equations_with_1_solutions.append(equation)
        else:
            equations_with_2_solutions.append(equation)

    print("Рівняння, що не мають розв'язків: ")
    for equation in equations_with_0_solutions:
        print(f"solution of equation {equation} is {equation.solutions()}")

    print("=========================================")
    print("Рівняння, що мають один розв'язок: ")
    for equation in equations_with_1_solutions:
        print(f"solution of equation {equation} is {equation.solutions()}")

    print("=========================================")
    print("Рівняння, що мають два розв'язки: ")
    for equation in equations_with_2_solutions:
        print(f"solution of equation {equation} is {equation.solutions()}")

    print("=========================================")
    print("Рівняння, що мають нескінченну кількість розв'язків: ")
    for equation in equations_with_Inf_solutions:
        print(f"solution of equation {equation} is {equation.solutions()}")

    equation_with_min_solution = equations_with_1_solutions[0]
    min_sol = equation_with_min_solution.solutions()[0]

    equation_with_max_solution = equations_with_1_solutions[0]
    max_solution = equation_with_min_solution.solutions()[0]

    for equation in equations_with_1_solutions[1:]:
        solutions = equation.solutions()
        if solutions[0] < min_sol:
            equation_with_min_solution = equation
            min_sol = solutions[0]

        if solutions[0] > max_solution:
            equation_with_max_solution = equation
            max_solution = solutions[0]

    print("==================================")
    print(f"з усіх рівнянь, що мають рівно один розв’язок,"
          f" рівняння {equation_with_min_solution} "
          f"має найменший розв'язок {min_sol} ")

    print("==================================")
    print(f"з усіх рівнянь, що мають рівно один розв’язок,"
          f" рівняння {equation_with_max_solution} "
          f"має найбільший розв'язок {max_solution} ")

