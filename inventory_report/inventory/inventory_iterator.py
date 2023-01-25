from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.__index = 0

    def __next__(self):
        result = self.iterable[self.__index]
        self.__index += 1
        return result
