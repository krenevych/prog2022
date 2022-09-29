x1, y1, x2, y2, a = [float(d) for d in input().split()]
x3 = (a * x2 + x1) / (a + 1)
y3 = (a * y2 + y1) / (a + 1)
print("%0.2f"% x3, "%0.2f"% y3)