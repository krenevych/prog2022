# Напишіть програму, що виводить на
# екран введене з клавіатури дійне
# число з 5 знаками після коми.

x = input("Введіть дійсне число ")
x = float(x)
# print("Число з п'ятьма знаками після коми = %f", x)
print("Число з п'ятьма знаками після коми = %0.5f" % x)