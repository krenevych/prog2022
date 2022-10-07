# n = 12345  # sum = 15, dob = 120, answer: 120 / 15

n = int(input())

sum = 0
dob = 1

while n > 0:
    last = n % 10
    sum += last
    dob *= last
    n = n // 10

print("%0.3f" % (dob / sum))
