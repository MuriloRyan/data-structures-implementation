#You can't start an Stack with an None value (it will not count)

from typing import Any

class Node:
    def __init__(self, value=None, next_node=None) -> None:
        self.value = value
        self.next = None
    
    def _validate_node(self):
        return vars(self)

    def _as_index(self,index,total_length):
        self.distance_from_bottom = abs(1 - index)
        self.distance_from_top = total_length - index
        self.index = index

        return self

    def __repr__(self):
        return str(self.value)

class Stack:
    def __init__(self, first_value=None, Node_Class=Node) -> None:
        #it allow us to change which Node Object we will use (dependence injection)
        self.Node_Class = Node_Class

        #the first of all nodes
        self._first_node = self.Node_Class(value=first_value)
        self._last_node = self.Node_Class(value=first_value)

        self._state = "__empty__" if first_value == None else "__not_empty__"
    
    def _validate_node(self, object_var: Any) -> dict:
        try:
            if object_var._validate_node():
                return True
            else:
                return None
        except:
            return None
    
    def peak(self) -> Node:
        return self._last_node
    
    def is_empty(self) -> bool:
        return True if self._state == "__empty__" else False

    def push(self, value: Any) -> str:
        #if the first node is empty
        if self._first_node.value is None:
            self._first_node.value = value
            self._last_node = self._first_node
            self._state = "__not_empty__"
            return value

        #else, we create the next node
        new_node = self.Node_Class(value=value)

        #and we push it in the next of the first node (if is empty)
        if self._first_node.next is None:
            self._first_node.next = new_node
        
        #else, we run thought all nodes and push it in the last one
        else:
            current_node = self._first_node.next

            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

        self._last_node = self.Node_Class(value=value)
        self._state = "__not_empty__"
        return value

    def pop(self) -> str:
        #if the first node is empty
        if self._first_node is None:
            self._state = "__empty__"
            return None

        #if the second is empty
        if self._first_node.next is None:
            value = self._first_node.value
            self._first_node = self.Node_Class()
            self._last_node = self._first_node
            self._state = "__empty__"
            return value

        #else, we start to count from the first node
        current_node = self._first_node
        prev_node = None

        #while the node has a next
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next

        value = current_node.value
        prev_node.next = None
        self._last_node = self.Node_Class(value=prev_node.value)
        self._state = "__not_empty__"
        return value

    def __len__(self) -> int:
        first_is_valid = self._validate_node(self._first_node)

        i = 1 if first_is_valid and self._state == "__not_empty__" else 0

        current_node = self._first_node.next if first_is_valid else None

        #while the next value is not None, we add "," and the value of the Node
        while current_node:
            i+=1

            #the next node is the next node of the last one
            current_node = current_node.next
        
        #return the length 
        return i

    def __repr__(self) -> str:
        def is_string(value):
            if isinstance(value, str):
                return f"'{value}'"
            return value

        final_list = 'Stack('

        #if the stack is not null
        final_list += is_string(self._first_node.value) if self._state == "__not_empty__" else ''

        current_node = self._first_node.next if self._validate_node(self._first_node) else None

        try:
            #while the next value is not None, we add "," and the value of the Node
            while current_node:
                final_list += ''.join(f',{is_string(current_node.value)}')

                #the next node is the next node of the last one
                current_node = current_node.next
        except:
            pass

        #finish the str of the stack
        return str(final_list) + ")"
    
    def __getitem__(self, item) -> Node:
        #raise a exception if item (arg of stack[i]) is not int
        if not isinstance(item, int):
            raise
        
        #we start to count with the first node, and we start i=0
        current_node,i = self._first_node, 1
        while i < item:
            if not current_node.next:
                raise IndexError

            #an simple update o the node
            current_node = current_node.next
            i += 1

        return current_node._as_index(i,len(self))

    def __iter__(self):
        #we start to count with the first one
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