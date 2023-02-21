# from turtle import * # Підключаємо модуль turtle
import turtle

turtle.reset()      # Ініціалізуємо режим малювання

# === Малюємо квадрат ===

turtle.delay(1000)

turtle.down()       # Опускаємо перо
turtle.forward(50)  # Рухаємося вперед на 50 пікселів,
                    # тобто зображуємо першу сторону квадрата
turtle.left(90)     # Поворот вліво на 90 градусів
turtle.forward(50)  # Зображуємо другу сторону квадрата
turtle.left(90)     # Поворот вліво на 90 градусів
turtle.forward(50)  # Зображуємо третю сторону квадрата
turtle.left(90)     # Поворот вліво на 90 градусів
turtle.forward(50)  # Зображуємо четверту сторону квадрата
turtle.up()         # Підіймаємо перо
# === Зображення квадрата завершено ===

mainloop()       # Затримуємо вікно на екрані