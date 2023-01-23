def readFile(fileName):
    with open(fileName, encoding="utf-8") as f:
        for line in f:
            print(line.strip())


if __name__ == '__main__':
    readFile("input01.txt")
