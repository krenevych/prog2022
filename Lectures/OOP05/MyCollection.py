from Lectures.OOP05.MyCollectionIterator import MyCollectionIterator


class MyCollection:
    def __init__(self):
        self._myLIst = []

    def append(self, item):
        self._myLIst.append(item)

    # def __getitem__(self, item):  # d[12]
    #     return self._myLIst[item]

    def __str__(self):
        return str(self._myLIst)

    def __iter__(self):
        return MyCollectionIterator(self._myLIst)


if __name__ == '__main__':
    lst = MyCollection()
    lst.append(1)
    lst.append(2)
    lst.append(444)

    iterator = iter(lst)

    for el in lst:
        print(el)
