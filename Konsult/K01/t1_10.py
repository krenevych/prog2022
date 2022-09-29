import math

S, R1 = [float(d) for d in input().split()]

s2 = (math.pi * R1 ** 2) - S

R2 = (s2 / math.pi) ** 0.5

print ("%0.2f" % R2)

