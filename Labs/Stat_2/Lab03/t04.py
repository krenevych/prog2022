n = int(input())

# n = 12345678
k = 0 if n > 0 else 1   # щоб врахувати,
                        # якщо введене з клавіатури число є 0,
                        # яке має одну цифру

while n > 0:
    n = n // 10
    k += 1

print(k)

