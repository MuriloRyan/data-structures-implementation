from typing import Any

class Node:
    def __init__(self, value=None, next_node=None) -> None:
        self.value = value
        self.next = next_node
        self.nonce = None
        self.empty = True
    
    def _validate_node(self):
        return vars(self)

    def __repr__(self):
        return str(self.value)

class Stack:
    def __init__(self, first_value=None, Node_Class=Node) -> None:
        #it allow us to change which Node Object we will use (dependence injection)
        self.Node_Class = Node_Class

        #the first of all nodes
        self._first_node = self.Node_Class(first_value)
        self._last_node = None 

        self._state = "__empty__" if first_value == None else "__not_empty__"
    
    def _validate_node(self, object_var: Any):
        try:
            object_var._validate_node
            return True
        except:
            return None

    def push(self,value: Any) -> str:

        # if the first node has not an next value...
        if not self._first_node.next:
            #they receive an next value.
            self._first_node.next = self.Node_Class(value=value)
            self._last_node = self._first_node.next
        
        #if the first node is None, or if his value is equal None
        elif not self._first_node or self._first_node.value == None:

            self._first_node = self.Node_Class(value=value)
            self._last_node = self._first_node

        #else
        else:

            #we start to count using the next of the first (second)
            next_node = self._first_node.next
            
            #and while the next_node have an next
            while next_node.next:
                #we go to the next node
                next_node = next_node.next
            
            #when a node has not with an next node... the loop ends
            #that means this is the last node, so, we give him a last node
            next_node.next = self.Node_Class(value=value)
            self._last_node = next_node.next

        self._state == "__not_empty__"
        return value

    def pop(self) -> str:
        #if the first node is empty
        if self._first_node is None:
            self._state = "__empty__"
            return None
        
        #if the second node is empty
        elif not self._first_node.next:
            #we clear the last node
            excluded_value = self._first_node.value
            self._first_node = Node_Class()
            self._last_node = None
            self._state = "__empty__"

        #we start with the first node
        next_node = self._first_node
        #it represent the node that come before the last one
        prev_node = None

        #and while the next_node have an next...
        try:
            while next_node.next:

                #this is the current node
                prev_node = next_node
                #this is the next one
                next_node = next_node.next

            #if prev_node exists, we remove his next value (the last one)
            if prev_node:
                prev_node.next = None
                self._last_node = prev_node  # we update the last node

            #else, that means we have only the first and the second node existing 
            else:
                self._first_node.next = None
                self._last_node = self._first_node

            #we return the next value of the prev_node (so, the last of the stack)
            return next_node.value
        
        except:
            return excluded_value
    
    def __len__(self):
        first_is_valid = self._validate_node(self._first_node)

        i = 1 if first_is_valid else 0

        next_node = self._first_node.next if first_is_valid else None

        #while the next value is not None, we add "," and the value of the Node
        while next_node:
            i+=1

            #the next node is the next node of the last one
            next_node = next_node.next
        
        #finish the str of the stack
        return i

    def __repr__(self):
        final_list, i = 'Stack(',0

        #if the stack is not null
        final_list += str(self._first_node.value) if self._state == "__not_empty__" else ''

        next_node = self._first_node.next if self._validate_node(self._first_node) else None

        try:
            #while the next value is not None, we add "," and the value of the Node
            while next_node:
                final_list += ',' + str(next_node)
                i+=1

                #the next node is the next node of the last one
                next_node = next_node.next
        except:
            pass

        #finish the str of the stack
        return str(final_list) + ")"
