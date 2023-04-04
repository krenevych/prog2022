from Labs.Mat1.OOP06.ProtectedDictIntIterator import ProtectedDictIntIterator
from Labs.Mat1.OOP07.ProtectedDictIntError import ProtectedDictIntError, ProtectedDictIntChangeValueError, \
    ProtectedDictIntKeyNonIntegerError


class ProtectedDictInt:

    def __init__(self):
        self._dict = {}

    def __contains__(self, item):
        return item in self._dict

    def __len__(self):
        return len(self._dict)

    def __setitem__(self, key, value):
        if key in self:
            raise ProtectedDictIntChangeValueError(key, self[key], value)

        if type(key) != int:
            raise ProtectedDictIntKeyNonIntegerError(key)
        # self[key] = value так не можна, бо відбувається зациклення через рекурсію, треба кликати батьківський метод!
        self._dict[key] = value

    def __getitem__(self, item):
        return self._dict[item]

    def __str__(self):
        return str(self._dict)

    def __repr__(self):
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

    try:
        myDict[23] = "23"  # myDict.__setitem__(23, "23")  # правильно
        print(myDict)
        # myDict[23] = "33323"  # не допускається
        # myDict["1234"] = "ssfdgs"  # не допускається
        myDict[45.4] = "ssfdgs"  # не допускається
    except ProtectedDictIntChangeValueError as er:
        print("ProtectedDictIntChangeValueError:",  er)
        print(f"Ключ {er.key} існує у словнику зі значенням {er.old_value}. Нове значення {er.new_value}")
    except ProtectedDictIntKeyNonIntegerError as er:
        print(er)
        key_type = type(er.key)
        print(f"Тип ключа {key_type}. Необхідно int")





