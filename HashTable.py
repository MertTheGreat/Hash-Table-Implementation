class HashTable(object):
    def __init__(self, size):
        self.keyArray = [None] * size
        self.valueArray = [None] * size
        self.size = size
        self._index = 0

    def set(self, key, value):
        hashed_key = self.__hash__(key)
        if self.keyArray[hashed_key] is None:
            self.keyArray[hashed_key] = key
            self.valueArray[hashed_key] = value
        else:
            i = 0
            while self.valueArray[hashed_key + i] is not None:
                if i + hashed_key + 1 >= self.size:
                    i = 0
                else:
                    i += 1
                print(i)
                if self.valueArray[hashed_key + i] is None:
                    self.keyArray[hashed_key + i] = key
                    self.valueArray[hashed_key + i] = value
                    break

    def get(self, key):
        index = self.keyArray.index(key)
        return self.valueArray[index]

    def index(self, value):
        index = self.valueArray.index(value)
        return self.keyArray[index]

    def __iter__(self):
        """
        Making the class iterable
        """
        return self

    def __next__(self):
        """
        Next item for iteration
        """
        if self._index < self.size:
            self._index += 1
            return self.valueArray[self._index - 1]
        elif self._index == self.size:
            self._index = 0
            # End of Iteration
            raise StopIteration

    def __hash__(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])) % self.size

        return hash

