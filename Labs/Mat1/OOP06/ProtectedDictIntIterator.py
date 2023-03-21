class ProtectedDictIntIterator:

    def __init__(self, collection):
        self.collection = list(collection)
        self.collection.sort()
        self.cursor = 0

    def __next__(self):
        try:
            elem = self.collection[self.cursor]
            self.cursor += 1
            return elem
        except IndexError:
            raise StopIteration
