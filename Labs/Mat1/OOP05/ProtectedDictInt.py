class ProtectedDictInt(dict):

    def __setitem__(self, key, value):
        if key in self:
            raise RuntimeError("Зміна значення за ключем заборонена!")

        if type(key) != int:
            raise RuntimeError("Ключ словника може бути лише цілим числом")

        # self[key] = value так не можна, бо відбувається зациклення через рекурсію, треба кликати батьківський метод!
        super().__setitem__(key, value)


if __name__ == '__main__':
    myDict = ProtectedDictInt()
    # myDict = {}

    myDict[23] = "23"  # myDict.__setitem__(23, "23")  # правильно
    # myDict[23] = "33323"  # не допускається

    # myDict["1234"] = "ssfdgs"  # не допускається
    # myDict[45.4] = "ssfdgs"  # не допускається
    myDict[123] = "2222"

    # print(myDict[123])

    print(myDict)
    # myDict.update({23: 999, "Hello": "World"})
    # print(myDict)
