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



if __name__ == '__main__':
    readFile60("input01.txt")
