a, b, c, d, f  = [float(d) for d in input().split()]
p1 = (a + b + f) / 2
p2 = (d + c + f) / 2
S = (p1 * (p1 - a) * (p1 - b) * (p1 - f)) ** 0.5
S1 = (p2 * (p2 - d) * (p2 - c) * (p2 - f)) ** 0.5
S2 = S1 + S
print( "%0.4f" % S2 )