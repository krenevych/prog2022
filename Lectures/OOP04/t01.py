class Pet:
    def __init__(self, name):
        self._name = name
    def voice(self):
        print(f"{self._name}: Я базовий клас, я не вмію говорити")


class Cat(Pet):
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color
    def voice(self):
        print(f"{self._name}:  я {self._color} кіт і я нявкаю")


if __name__ == '__main__':
    # p = Pet("Базеус")
    # p.voice()

    c = Cat("Кузя", "black")
    c.voice()

