# 865 + 568 = 1433 - не паліндром
# 1433 + 3341 = 4774 - паліндром

m = int(input())
# m = 865
palindrom_rate = 0
while True:
    tmp_m = m
    inv_m = 0
    while tmp_m > 0:
        last = tmp_m % 10
        inv_m = inv_m * 10 + last
        tmp_m = tmp_m // 10
    if m == inv_m:
        break

    m = m + inv_m
    palindrom_rate += 1

print(palindrom_rate)