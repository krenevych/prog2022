# n = 442
# n = 222
n = 918

od = n % 10
de = n // 10 % 10
so = n // 100

cond_a = od == 2 or de == 2 or so == 2
# cond_all2 = od == 2 and de == 2 and so == 2
# cond_all2 = n == 222

print("a)", cond_a)

cond_b = od % 2 == 0 and de % 2 == 0 and so % 2 == 0
print("b)", cond_b)

cond_c = od + de + so == 18
print("c)", cond_c)