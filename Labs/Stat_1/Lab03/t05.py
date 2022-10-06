n = int(input())
# n = 12345

sum = 0
dob = 1

while n > 0:
    last = n % 10

    sum += last
    dob *= last

    n = n // 10

print("%0.3f" % (dob / sum))


