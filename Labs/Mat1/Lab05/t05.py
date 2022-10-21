a1 = [int(el) for el in input().split()]
a2 = [int(el) for el in input().split()]

# a1 = [x0,       y0,    x1,    y1]
# a1 = [a1[0], a1[1], a1[2], a1[3]]
#          5      1      2      6

# 1 1 7 8
#          x              y
u = [a2[2] - a2[0], a2[3] - a2[1]]   # [-3, 5]
v = [a1[2] - a1[0], a1[3] - a1[1]]   # [6,  7]