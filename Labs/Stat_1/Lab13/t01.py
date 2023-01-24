def readFile(file_name):
    with open(file_name, "rt",  encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            print(line)




readFile("input01.txt")
print("============")
