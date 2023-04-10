class Movable:
    def move(self):
        print(f"{self._name} I can move on the road")

class MovableByWatter:
    def move(self):
        print(f"{self._name} I can move by the watter")



class Car:

    def __init__(self, name):
        self._name = name

    def helloFromCar(self):
        print(f"Car{self._name}: Hello")

class Motorcicle:
    def __init__(self, name):
        self._name = name
    def helloFromMoto(self):
        print(f"Moto{self._name}: Hello")

class MovableCar(Car, Movable):
    pass

class WatterMotorcicle(Motorcicle, MovableByWatter):
    pass

class MovableMoto(Motorcicle, Movable):
    pass

if __name__ == '__main__':
    car = Car("Zaz")
    car.helloFromCar()
    moto = Motorcicle("KMZ")
    moto.helloFromMoto()

    movableCar = MovableCar("MovableZaz")
    movableCar.move()

    movableMoto = MovableMoto("MovableKMZ")
    movableMoto.move()

    watterMoto = WatterMotorcicle("Honda")
    watterMoto.move()
