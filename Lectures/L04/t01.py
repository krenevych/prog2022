# Знайти суму цифр заданого натурального числа
N = int(input())
# N = 1234

tmp_N = N
suma = 0
while tmp_N > 0:
    last = tmp_N % 10
    suma += last
    tmp_N = tmp_N // 10

print("Сума цифр числа %d є %d" % (N, suma))


