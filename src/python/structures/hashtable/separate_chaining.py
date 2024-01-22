#not working fully

from hashtable.index_class import Index

class SeparateChainingHashTable:
    def __init__(self, length, index_class=Index):
        self.index_class = index_class
        self.length = length
        self.data = [ self.index_class() for _ in range(self.length)]
    
    def _hash(self, key):
        key = str(key)
        final_key = ''
        
        for c in key:
            final_key += str(ord(c))
            
        key = int(final_key)

        return key % (self.length-1)

    def append(self, value, key):
        self.data[self._hash(key)].add_value(value)
        return True

    def remove(self, value, key):
        self.data[self._hash(key)] = self.index_class()
        return True

    def __getitem__(self, index):
        return self.data[index]

    def __repr__(self):
        str_repr = 'HashTable('
        for index in self.data:
            str_repr += str(str(index) + ',') if len(index) != 0 else str(str(None) + ',')

        return str_repr + ')'

