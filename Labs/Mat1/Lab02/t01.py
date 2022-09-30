n = 76

condition_a = n % 2 == 0
print("a)", condition_a)

condition_b = n % 10 == 0
print("b)", condition_b)

od = n % 10
de = n // 10
condition_c = od + de > 9
print("c)", condition_c)
