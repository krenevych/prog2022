N = int(input("N = "))

with open("out.txt", "w") as f_out:
    i = 1
    while i ** 2 <= N:
        print(i ** 2, file=f_out)
        i += 1
