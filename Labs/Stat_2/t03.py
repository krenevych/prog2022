# Проста задача?
# https://www.e-olymp.com/uk/problems/1
# Програма зчитує двоцифрове число і виводить через
# пропуск кожну цифру окремо.
# Вхідні дані
# Натуральне число на проміжку від 10 до 99 включно.
# Вихідні дані
# Спочатку першу цифру числа і через пропуск другу.

# n = 23
n = int(input())

m = n // 10 # перша цифра
k = n % 10  # друга цифра

print(m, k)