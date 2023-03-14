class ProtectedDictInt:

    def __init__(self):
        self._dict = {}

    def __contains__(self, item):
        return item in self._dict

    def __len__(self):
        return len(self._dict)

    def __setitem__(self, key, value):
        if key in self:
            raise RuntimeError("Зміна значення за ключем заборонена!")

        if type(key) != int:
            raise RuntimeError("Ключ словника може бути лише цілим числом")

        # self[key] = value так не можна, бо відбувається зациклення через рекурсію, треба кликати батьківський метод!
        self._dict[key] = value

    def __getitem__(self, item):
        return self._dict[item]

    def __str__(self):
        return str(self._dict)

    def __add__(self, other):
        resultDict = ProtectedDictInt()
        for k, v in self._dict.items():
            resultDict[k] = v

        if isinstance(other, tuple):
            resultDict[other[0]] = other[1]
        elif isinstance(other, ProtectedDictInt):
            for key, val in other._dict.items():  # TODO: змінити на цикл по словнику після реалізації ітераційного протоколу для нашого словника
                resultDict[key] = val
        else:
            raise RuntimeError("Тип другого операнда має бути або кортеж або ProtectedDictInt")

        return resultDict

    def __sub__(self, other):
        if type(other) != int:
            raise RuntimeError("Тип другого операнда має збігатися з типом ключів (int) словника ProtectedDictInt")

        resultDict = ProtectedDictInt()
        for k, v in self._dict.items():
            if k != other:
                resultDict[k] = v

        return resultDict


if __name__ == '__main__':
    myDict = ProtectedDictInt()
    # myDict = {}

    myDict[23] = "23"  # myDict.__setitem__(23, "23")  # правильно
    # myDict[23] = "33323"  # не допускається

    # myDict["1234"] = "ssfdgs"  # не допускається
    # myDict[45.4] = "ssfdgs"  # не допускається
    myDict[123] = "2222"

    print(myDict[123])

    print(myDict)
    # myDict.update({23: 999, "Hello": "World"})
    # print(myDict)

    print(len(myDict))

    myDict2 = ProtectedDictInt()
    myDict2[1] = 1
    myDict2[11] = 11
    print(myDict2)

    newMyDict = myDict + myDict2
    print(newMyDict)

    newMyDict2 = myDict + (2, 44)
    print(newMyDict2)

    newMyDict3 = newMyDict2 - 2
    print(newMyDict3)

