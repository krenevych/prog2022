class MyClass:
    def __init__(self):
        self.lst = []

    def add(self, elem):
        self.lst.append(elem)

    def __str__(self):
        return str(self.lst)


from copy import copy, deepcopy

if __name__ == '__main__':
    obj1 = MyClass()
    obj1.add(10)
    obj1.add(11)
    obj1.add(12)
    print("obj1 = ", obj1)
    # obj2 = copy(obj1)
    obj2 = deepcopy(obj1)
    print("obj2 = ", obj2)
    obj2.add(122)
    print("obj1 = ", obj1)
    print("obj2 = ", obj2)
