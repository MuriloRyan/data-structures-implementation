class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return self.value

class LinkedList:
    def __init__(self, node_class=Node):
        self.node_class = node_class

        self.head = node_class(None)
        self.last_node = self.head

    def append(self,value):
        if self.head.value == None:
            next_node = self.node_class(value)
            self.head = next_node
            return value
        
        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = self.node_class(value)
        return value

    def pop(self):
        if self.head.next == None:
            value = self.head.value
            self.head = self.node_class(None)
            return value
        
        current_node = self.head
        
        while current_node.next:
            last_node = current_node
            current_node = current_node.next
        
        value = last_node.value
        last_node.next = None
        return value
    
    #__getitem__()
    def get(self, index):
        return self[index]
    
    def search(self, value):
        current_node, i = self.head, 0

        try:
            while current_node.value != value:
                current_node = current_node.next
                i+=1

        except:
            return None

        return {'value': current_node.value, 'index': i}
    
    #__delitem__()
    def remove(self, index):
        del self[index]
    
    #set: LinkedList[i]=value; get LinkedList[i]; del: del LinkedList[i].
    def __setitem__(self, index, value):
        current_node, i = self.head, 1

        while i < index:
            if not current_node.next:
                raise IndexError
            
            current_node, i = current_node.next, i+1

        current_node.value = value
        return current_node

    def __getitem__(self, index):
        current_node, i = self.head, 1

        while i <= index:
            if not current_node.next:
                raise IndexError

            current_node, i = current_node.next, i+1

        return current_node
    
    def __delitem__(self, index):
        if index < 0:
            raise IndexError("Index out of range")

        if index == 0:
            # Special case for deleting the head
            if self.head.next:
                self.head = self.head.next
            else:
                # If the list has only one element, reset the head
                self.head = self.node_class(None)
            return

        current_node, i = self.head, 0

        while i < index - 1:
            if not current_node.next:
                raise IndexError("Index out of range")
            
            current_node, i = current_node.next, i + 1

        if not current_node.next:
            raise IndexError("Index out of range")

        current_node.next = current_node.next.next

    def __iter__(self):
        self._iter_index = 1
        return self
    
    def __next__(self):
        #return Stack[i]
        try:
            value = self[self._iter_index]
            self._iter_index += 1
            return value
        
        except:
            raise StopIteration
    
    def __len__(self):
        current_node,i = self.head,1
        if not current_node.value:
            return 0

        if not current_node.next:
            return i

        while current_node.next:
            current_node = current_node.next
            i += 1

        return i

    def __repr__(self):
        def is_string(value):
            if isinstance(value, str):
                return f"'{value}'"
            return value

        final_string = 'LinkedList('

        current_node, i = self.head, 0
        if current_node.value == None:
            return final_string + ')'

        while current_node:
            final_string += f'{is_string(current_node.value)},'
            current_node = current_node.next

        return str(final_string)[:-1] + ')'

