# Напишіть програму, що виводить на екран
# введене з клавіатури дійне число
# з 5 знаками після коми.

x = input("Введіть дійсне число ")
x = float(x)

print("Дійсне число = %0.5f" % (x))