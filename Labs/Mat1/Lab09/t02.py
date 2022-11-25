n = int(input())
elems = [int(e) for e in input().split()]

# print(elems)

# словник частот входження чисел.
freq = {}
for el in elems:
    if el in freq:
        continue

    freq[el] = elems.count(el)

# print(freq)
n_2 = n // 2
for key, val in freq.items():
    if val > n_2:
        print(key)
        break
else:
    print(-1)

