def sumInFile(file_name):
    suma = 0
    with open(file_name) as f:
        for line in f:
            # print(line.split())
            suma += sum([float(el) for el in line.split()])
    return suma


if __name__ == '__main__':
    print(sumInFile("input02.txt"))
