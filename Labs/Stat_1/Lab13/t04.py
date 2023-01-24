def readMatrix(file_name):
    M = []

    with open(file_name) as f:
        for line in f:
            row = [float(el) for el in line.split()]
            M.append(row)

    return M


def writeMaxtixToFile(M, file_name):
    with open(file_name, "w") as f:
        for row in M:
            print(*row, sep="   ", file=f)

def sumMatrix(A, B):
    return [  # Stub
        [1, 2],
        [3, 4]
    ]

########################################
if __name__ == '__main__':
    A = readMatrix("input04.txt")
    B = readMatrix("input04_2.txt")
    C = sumMatrix(A, B)
    writeMaxtixToFile(C, "output04.txt")
