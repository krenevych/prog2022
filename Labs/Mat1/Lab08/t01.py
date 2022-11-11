# 0! = 1
# 5! = 4! * 5
#      ||
#      3! * 4
#      ||
#      2! * 3
#      ||
#      1! * 2
#      ||
#      0! * 1
#      ||
#      1
def Fact(n):
    if n == 0:
        return 1
    else:
        return Fact(n-1) * n
    
f = Fact(5)
print(f)
