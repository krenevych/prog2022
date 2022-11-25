# 7
# 3 3 3 3 3 5 -7 7 5 -9 -4

n = int(input())
elems = [int(e) for e in input().split()]
# elems.remove(3)

elem_set_freq_more_than_one_time = set() # множина елементів, що трапляються в списку більше одного разу
for el in elems:
    # elems.remove(el) # NEVER!!!! ніколи не змінювати в циклі for по колекції колецію яку інтерує цей цикл

    if el in elem_set_freq_more_than_one_time:
        continue

    if elems.count(el) == 1:
        print(el, end=" ")
    else:
        elem_set_freq_more_than_one_time.add(el)

# print()
# print(elem_set_freq_more_than_one_time)
