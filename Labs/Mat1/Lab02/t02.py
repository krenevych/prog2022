n = 256

od = n % 10
de = n // 10 % 10
so = n // 100

condition_a = od == 2 or de == 2 or so == 2
print("a)", condition_a)

# condition_all2 = n == 222
# print("condition_all2", condition_all2)

condition_b = od % 2 == 0 and de % 2 == 0 and so % 2 == 0
print("b)", condition_b)

condition_c = od + de + so == 18
print("c)", condition_c)
