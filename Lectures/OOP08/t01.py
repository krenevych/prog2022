from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):

    @abstractmethod
    def myMethod(self, pram1, param2):
        pass


class ConcreteClass(AbstractClass):
    def myMethod(self, pram1, param2):
        print("myMethod from ConcreteClass")


if __name__ == '__main__':
    abstractClass = ConcreteClass()
    abstractClass.myMethod(1, 2)
