n = int(input())
elems = [int(e) for e in input().split()]

elem_set_more_than_1 = set()
for el in elems:
    if el in elem_set_more_than_1:
        continue

    count = elems.count(el)
    if count > 1:
        elem_set_more_than_1.add(el)

new_elems = []
for el in elems[::-1]:
    if el in elem_set_more_than_1:
        new_elems.append(el)
        elem_set_more_than_1.remove(el)

if len(new_elems) > 0:
    print(*new_elems[::-1])
else:
    print("NO")
