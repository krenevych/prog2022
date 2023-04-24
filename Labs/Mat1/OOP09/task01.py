from abc import ABCMeta, abstractmethod


class Spy(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def visitGeneralStaff(self, militaryObject):
        pass

    @abstractmethod
    def visitMilitaryBase(self, militaryObject):
        pass

class SecretAgent(Spy):
    def __init__(self, name):
        super().__init__(name)
        self.information = ""

    def visitGeneralStaff(self, militaryObject):
        self.information = f"GeneralStaff: У генеральному штабі є {militaryObject.generals} геренералів та {militaryObject.secretPaper} секретних паперів."

    def visitMilitaryBase(self, militaryObject):
        self.information = f"MilitaryBase: На військовій базі є {militaryObject.officers} офіцерів, {militaryObject.soldiers} солдатів, {militaryObject.jeeps} джипів та {militaryObject.tanks} танків."

    def __str__(self):
        return self.name + f":\n{self.information}"

class Saboteur(Spy):

    def visitGeneralStaff(self, militaryObject):
        print(f"{self.name}: Усіх замочу, нікого не лишу!")
        militaryObject.generals = 0
        militaryObject.secretPaper = 0

    def visitMilitaryBase(self, militaryObject):
        print(f"{self.name}: Бавовна понад усе!")
        militaryObject.jeeps = 0
        militaryObject.tanks = 0
        militaryObject.officers = 0
        militaryObject.soldiers = 0

class MilitaryObject(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, spy):
        pass


class GeneralStaff(MilitaryObject):
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def accept(self, spy: Spy):
        spy.visitGeneralStaff(self)


class MilitaryBase(MilitaryObject):
    def accept(self, spy: Spy):
        spy.visitMilitaryBase(self)

    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks


if __name__ == '__main__':
    james_bond = SecretAgent("James Bond")

    generalStaff = GeneralStaff(20, 100)
    generalStaff.accept(james_bond)
    print(james_bond)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    militaryBase.accept(james_bond)
    print(james_bond)

    Budanov = Saboteur("Budanov")
    generalStaff.accept(Budanov)
    militaryBase.accept(Budanov)

    print("=== Після бавовни ..... ")

    generalStaff.accept(james_bond)
    print(james_bond)

    militaryBase.accept(james_bond)
    print(james_bond)
