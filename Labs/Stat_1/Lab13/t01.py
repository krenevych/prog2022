def readFile(file_name):
    with open(file_name, "rt", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            print(line)


def printMore60(file_name):
    with open(file_name, "rt", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if len(line) > 60:
                print(line)


def countEmpty(file_name):
    with open(file_name, "rt", encoding='utf-8') as f:
        return [line.strip() for line in f].count("")


def findMaxLen(file_name):
    maxLine = ""
    with open(file_name, "rt", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if len(line) > len(maxLine):
                maxLine = line

    return maxLine


# readFile("input01.txt")
# printMore60("input01.txt")
# print(countEmpty("input01.txt"))
print(findMaxLen("input01.txt"))

print("============")
