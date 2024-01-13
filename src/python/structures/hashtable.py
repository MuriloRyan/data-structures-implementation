"""   I will create a factory function
    to return the correct type of HashTable
    like: separate chaining HT and open addressing HT

    for now, the Hashtable class is an separate chaining hash table
"""

class Index:
    def __init__(self):
        self.value = []
    
    def add_value(self, value):
        self.value.append(value)
        return value

    def __len__(self):
        i = 0
        for item in self.value:
            i += 1

        return i

    def __repr__(self):
        return str(self.value)

#Separate chaining Hash table
class HashTable:
    def __init__(self, length, index_class=Index):
        self.index_class = index_class
        self.length = length
        self.data = [ self.index_class() for _ in range(self.length)]
    
    def _hash(self, key):
        return key % (self.length-1)

    def append(self, value, key):
        self.data[self._hash(key)].add_value(value)
        return True

    def remove(self, value, key):
        self.data[self._hash(key)] = self.index_class()
        return True

    def __repr__(self):
        str_repr = 'HashTable('
        for index in self.data:
            str_repr += str(str(index) + ',') if len(index) != 0 else str(str(None) + ',')

        return str_repr + ')'
