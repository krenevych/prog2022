#               | 0, n == 0
# mult(n, m) =  {
#               \ mult(n-1, m) + m

def mult(n, m):
    if n == 0:
        return 0
    else:
        return mult(n-1, m) + m

print(mult(3, 4))