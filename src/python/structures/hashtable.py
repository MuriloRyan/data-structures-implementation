# 11/30/2023
from typing import Any
import sys

class Node:
    def __init__(self, init_value=None) -> None:
        self.value = [init_value]
    
    def add_value(self, value: Any):
        if self.value[0] == None and len(self.value) == 1:
            self.value = [value]

            return True

        self.value.append(value)
        return True

    def __repr__(self):
        return str(self.value)

class Hashtable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.data = [Node() for _ in range(size)]

    def _hash(self, key: str) -> int:
        pre_hash = 0
        primo = 33
        
        for c in key:
        	pre_hash = (pre_hash + ord(c) * primo ) % self.size
        
        index = pre_hash
        return index

    def put(self, key: str, value: Any):
        index = self._hash(key)
        
        self.data[index].add_value(value)
        return True
        
    def get(self, key: str) -> Any:
        index = self._hash(key)
        data = self.data[index]

        return {
            "data": data,
            "index": index
        }
        
    def kill_one(self, key: str, value: Any):
        index = self._hash(key)

        try:
            node = self.data[index]
            node.value.remove(value)

            if len(node.value) == 0:
                node.value = [None]
            
            return True
        except:
            return False
    
    def clear(self, index=None, key=None):
    	index = index if index else self._hash(key)
    	
    	self.data[index] = Node()
     	
    	return True
    	
    def memory_bytes(self) ->int:
    	total_size = 0
    	
    	for iten in self.data:
    		node = iten
    		total_size += sys.getsizeof(node)
    	
    	return total_size

    def __repr__(self) -> str:
        
        things = ''
        for i in self.data:
            if not i:
                things += 'None,'
            else:
                things += str(i) + ','
        return f'({things})'
        
    def __len__(self) -> int:
     	return self.size
     	
    def line(self):
     	result, i = '', 0
     	
     	for node in self.data:
     		result += f"{i} - {node}\n"
     		i += 1
     	
     	return result

if __name__=='__main__':

    ht = Hashtable(16)

    ht.put('testing','apple')

    print('\n', ht, '\n')

    print(ht.get('testing'), '\n')

    print (ht.kill_one('testing','apple'))

    print(ht, '\n')