from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

def parseInputFile(file_name):
    equations = []
    with open(file_name) as f:
        for line in f:
            coefs = [int(elem) for elem in line.split()]
            if len(coefs) == 2:
                equations.append(Equation(*coefs))
            elif len(coefs) == 3:
                equations.append(QuadraticEquation(*coefs))
            elif len(coefs) == 5:
                equations.append(BiQuadraticEquation(coefs[0], coefs[2], coefs[4]))


    return equations


    # Для заданого набору квадратних рівнянь, покажіть ті з них, що:
equations_with_0_solutions = []    # •	не мають розв’язків;
equations_with_1_solutions = []    # •	мають один розв’язок;
equations_with_2_solutions = []    # •	мають два розв’язки;
equations_with_3_solutions = []    # •	мають три розв’язки;
equations_with_4_solutions = []    # •	мають чотири розв’язки;
equations_with_Inf_solutions = []  # •	мають нескінченну кількість розв’язків.

if __name__ == '__main__':
    equations = parseInputFile("input01.txt")
    for eq in equations:
        # print("------------------")
        # print(eq)
        # print(eq.solve())
        sols = eq.solve()
        if sols == Equation.INF:
            equations_with_Inf_solutions.append(eq)
        else:
            number_sols = len(sols)
            if number_sols == 0:
                equations_with_0_solutions.append(eq)
            elif number_sols == 1:
                equations_with_1_solutions.append(eq)
            elif number_sols == 2:
                equations_with_2_solutions.append(eq)
            elif number_sols == 3:
                equations_with_3_solutions.append(eq)
            elif number_sols == 4:
                equations_with_4_solutions.append(eq)

    print("Рівняння, що не мають розв'язків: ")
    for equation in equations_with_0_solutions:
        print(f"solution of equation {equation} is {equation.solve()}")

    print("=========================================")
    print("Рівняння, що мають один розв'язок: ")
    for equation in equations_with_1_solutions:
        print(f"solution of equation {equation} is {equation.solve()}")

    print("=========================================")
    print("Рівняння, що мають два розв'язки: ")
    for equation in equations_with_2_solutions:
        print(f"solution of equation {equation} is {equation.solve()}")

    print("=========================================")
    print("Рівняння, що мають три розв'язки: ")
    for equation in equations_with_3_solutions:
        print(f"solution of equation {equation} is {equation.solve()}")

    print("=========================================")
    print("Рівняння, що мають чотири розв'язки: ")
    for equation in equations_with_4_solutions:
        print(f"solution of equation {equation} is {equation.solve()}")

    print("=========================================")
    print("Рівняння, що мають нескінченну кількість розв'язків: ")
    for equation in equations_with_Inf_solutions:
        print(f"solution of equation {equation} is {equation.solve()}")
