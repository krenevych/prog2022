class MyCollectionIterator:
    def __init__(self, collection):
        self.collection = collection
        self.cursor = 0

    def __next__(self):
        try:
            result = self.collection[self.cursor]
            self.cursor += 1
            return result
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    lst = [1, 2, 3]

    # for el in lst:
    #     print(el)

    iterator = MyCollectionIterator(lst)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

