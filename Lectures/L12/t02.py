f = open("input02.txt")

suma = 0
for line in f:
    suma += int(line)
f.close()

print(suma)
