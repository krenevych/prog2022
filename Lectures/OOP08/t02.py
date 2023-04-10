from abc import ABCMeta, abstractmethod

class CanMakeSound(metaclass=ABCMeta):

    @abstractmethod
    def voice(self):
        pass


class Cat(CanMakeSound):
    def voice(self):
        print("Miu")

class Human(CanMakeSound):

    def voice(self):
        print("To be or not to be, this is the question!")



if __name__ == '__main__':
    c = Cat()
    h = Human()

    c.voice()
    h.voice()

