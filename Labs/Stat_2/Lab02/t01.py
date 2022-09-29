# a)
n = int(input("n = "))

is_even = n % 2 == 0
print(is_even)

# b)
n = 306
is_last_digit_0 = n % 10 == 0
print(is_last_digit_0)

# c)
n = 23
de = n // 10
od = n % 10
is_sum_greter_then_10 = de + od > 9
print(is_sum_greter_then_10)
