from index_class import Index

class Index(Index):
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.collisions = []

    def add_collision(self, value, key, steps):
        self.collisions.append({
            "value": value,
            "key": key,
            "steps": steps
        })
    
    def remove_collision(self, value, key):
        self.collisions.remove(value, key)

class LinearProbingSeparateChainingHashTable:
    def __init__(self, length, index_class=Index):
        self.index_class = index_class
        self.length = length
        self.data = [ None for _ in range(self.length)]
    
    def _hash(self, key):
        key = str(key)
        final_key = ''
        
        for c in key:
            final_key += str(ord(c))
            
        key = int(final_key)

        return key % (self.length-1)

    def append(self, value, key):
        index = self._hash(key)

        if self.data[index] == None:
            self.data[index] = self.index_class(value, key)

            return True
        
        i = index
        try:
            while True:
                if self.data[i] == None:
                    break

                i += 1

            self.data[i] = self.index_class(value, key)
            self.data[index].add_collision(value, key, (i-index))
            return True

        except IndexError:
            return False

    def remove(self, value, key):
        index = self._hash(key)
        index_data = self.data[index]

        if index_data is None:
            return False

        if value == index_data.value and key == index_data.key:
            self.data[index] = None
            return True

        for collision in index_data.collisions:
            if value == collision["value"] and key == collision["key"]:
                index_data.collisions.remove(collision)
                return True

        return False

    def __repr__(self):
        str_repr = 'HashTable('
        for index in self.data:
            str_repr += str(str(index) + ',')

        return str_repr + ')'


ht = LinearProbingSeparateChainingHashTable(25)

for i in range(25):
    print(ht.append(str(i), str(i)), i)

print(ht)

for i in range(12):
    print(ht.remove(str(i), str(i)))

print(ht)