class MyCollection:
    def __init__(self):
        self._myDict = {}

    def __setitem__(self, key, value):
        self._myDict[key] = value

    def __getitem__(self, item):
        return self._myDict[item]

    def __str__(self):
        return str(self._myDict)


if __name__ == '__main__':
    d = MyCollection()
    # d = {}
    d[1] = 1
    d[2] = 2
    print(d)
    # print(d[1])
    for el in d:
        print(el)
