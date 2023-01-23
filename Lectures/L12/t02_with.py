suma = 0

with open("input02.txt") as f:  # f = open("input02.txt")
    for line in f:
        suma += int(line)

print(suma)
