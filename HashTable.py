class HashTable(object):
    def __init__(self, size):
        """
        Hash Table constructor
        :param size: size of the table must be given
        """
        self.keyArray = [None] * size
        self.valueArray = [None] * size
        self.size = size
        self._index = 0

    def set(self, key, value):
        """
        Setter for hash table. Open Addressing used for collisions.
        :param key: key
        :param value: value
        :return: Hash Table value
        """
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
        """
        Getter for Hash Table item
        :param key: key
        :return: value
        """
        index = self.keyArray.index(key)
        return self.valueArray[index]

    def index(self, value):
        """
        Getter for index of the value
        :param value: value
        :return: key
        """
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
        """
        The Hash Function. Linear Probing used for the Hash Function
        :param key:
        :return:
        """
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])) % self.size

        return hash

