from Labs.Mat1.OOP06.ProtectedDictIntIterator import ProtectedDictIntIterator


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
        for k in self:
            v = self[k]
            resultDict[k] = v

        if isinstance(other, tuple):
            resultDict[other[0]] = other[1]
        elif isinstance(other, ProtectedDictInt):
            for key in other:
                val = other[key]
                resultDict[key] = val
        else:
            raise RuntimeError("Тип другого операнда має бути або кортеж або ProtectedDictInt")

        return resultDict

    def __sub__(self, other):
        if type(other) != int:
            raise RuntimeError("Тип другого операнда має збігатися з типом ключів (int) словника ProtectedDictInt")

        resultDict = ProtectedDictInt()
        for k in self:
            if k != other:
                resultDict[k] = self[k]

        return resultDict

    def __iter__(self):
        return ProtectedDictIntIterator(self._dict)


if __name__ == '__main__':
    myDict = ProtectedDictInt()
    # myDict = {}

    myDict[23] = "23"
    myDict[123] = "2222"
    myDict[77] = "Hello, world!"

    for key in myDict:
        print(f"{key}: {myDict[key]}")

    # iterMyDict = iter(myDict)
    # while True:
    #     try:
    #         key = next(iterMyDict)
    #         print(f"{key}: {myDict[key]}")
    #     except StopIteration:
    #         break

    myDict2 = ProtectedDictInt()
    myDict2[1] = 1
    myDict2[11] = 11

    newMyDict = myDict + myDict2
    print(newMyDict)

    for key in newMyDict:
        print(f"{key}: {newMyDict[key]}")
