class MyIndexError(IndexError):
    def __init__(self, message, index):
        self.message = message
        self.index = index

    def __str__(self):
        return f"{self.message}: {self.index}"

    def myMethodForThisException(self):
        print("Hello")

def getFromList(lst, index):
    try:
        return lst[index]
    except IndexError:
        raise MyIndexError("Індекс занадто великий", index)


if __name__ == '__main__':
    lst = [1, 2, 3]

    try:
        print(getFromList(lst, 5))
        # print(lst[88])

    except IndexError as er:
        print("Error:", er)
        if isinstance(er, MyIndexError):
            er.myMethodForThisException()
