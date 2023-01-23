

with open("output03.txt", "w") as f:
    for i in range(1, 10):
        print(str(i)*i, file=f)
