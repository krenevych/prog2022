def readFile(fileName):
    with open(fileName, encoding="utf-8") as f:
        for line in f:
            print(line.strip())


def readFile60(fileName):
    with open(fileName, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) > 60:
                print(line)


def countEmpty(fileName):
    counter = 0
    with open(fileName, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                counter += 1
    return counter


if __name__ == '__main__':
    print(countEmpty("input01.txt"))
