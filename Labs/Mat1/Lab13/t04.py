def readMatrix(inputFile):
    M = []
    with open(inputFile) as f:
        for line in f:
            row = [float(el) for el in line.split()]
            M.append(row)

    return M


def writeMatrixToFile(M, fileName):
    with open(fileName, 'w') as f:
        for row in M:
            print(*row, sep="   ", file=f)


if __name__ == '__main__':
    M = readMatrix("input04.txt")
    writeMatrixToFile(M, "output04.txt")
