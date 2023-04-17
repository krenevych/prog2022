N = int(input("N = "))

b = 9
c = 2
an1 = 3  # попередній a_n-1
an2 = 1  # перед-попередній  a_n-2
an3 = 1  # перед-перед-попередній  a_n-3
P = 1/9

#        an3
#             an2
#                   an1
#                    a
# 1   1   3  1+1/4   r

for n in range(3, N+1):
    b *= 3  # b = 3 * b
    c *= 2  # c = 2 * c
    # a = an3 + an2 / c
    # an3 = an2
    # an2 = an1
    # an1 = a
    #
    #     an3
    #        an2
    #            an1
    # 1   1   3  1+1/4

    an1, an2, an3 = an3 + an2 / c, an1, an2
    P = P * an1 / b

print(f"P_{N} = {P}")


