
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

condition_of_triangle_existence = ((a > 0)
                                   and (b > 0)
                                   and c > 0
                                   and (a + b > c)
                                   and (b + c > a)
                                   and (a + c > b))

print(condition_of_triangle_existence)
