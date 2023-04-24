from tkinter import *

from Labs.Mat1.OOP11.utils import isPalindrom


def callback():
    # print("Hello!")
    content = ent.get()

    # print(f"{content} is palindrom = {isPalindrom(content)}" )
    lab['text'] = f"{content} is palindrom = {isPalindrom(content)}"


if __name__ == '__main__':
    root = Tk()  # створюємо головне вікно програми

    btn = Button(root,  # контейнер, що містить
                 text="Click me",  # надпис на кнопці
                 width=20, height=5,  # ширина та висота
                 bg="white", fg="black",  # колір фону і напису
                 font="Arial 18",  # шрифт надпису та розмір
                 command=callback)  # функція обробки подій
    btn.pack()  # розміщення кнопки у головному вікні

    ent = Entry(root,  # батьківське вікно (контейнер)
                width=20,  # ширина поля
                bd=3,  # розмір границі
                bg="blue", fg="red",  # колір фону і напису
                font="Arial 18", )  # шрифр та розмір
    ent.pack()  # розміщення поля введення у головному вікні

    lab = Label(root,  # батьківське вікно (контейнер)
                width=20, height=5,  # ширина та висота
                text="Напис!",  # текст напису
                bd=5,  # розмір границі
                bg="blue", fg="red",  # колір фону і напису
                font="Arial 18")  # шрифр та розмір
    lab.pack()  # розміщення напису у головному вікні

    print("До root.mainloop()")
    root.mainloop()  # запускаємо цикл головного вікна
    print("Після root.mainloop()")
