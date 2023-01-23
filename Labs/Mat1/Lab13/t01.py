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


def find_the_longest_line(fileName):
    longest_line = ""
    with open(fileName, encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) >= len(longest_line):
                longest_line = line
    return longest_line


if __name__ == '__main__':
    print(find_the_longest_line("input01.txt"))
