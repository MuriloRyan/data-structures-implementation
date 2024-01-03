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
        self._first_node = self.Node_Class(value=first_value)
        self._last_node = self.Node_Class(value=first_value)

        self._state = "__empty__" if first_value == None else "__not_empty__"
    
    def _validate_node(self, object_var: Any):
        try:
            if object_var._validate_node():
                return True
            else:
                return None
        except:
            return None
    
    def peak(self):
        return self._last_node
    
    def is_empty(self):
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

    def __len__(self):
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

    def __repr__(self):
        final_list = 'Stack('

        #if the stack is not null
        final_list += str(self._first_node.value) if self._state == "__not_empty__" else ''

        current_node = self._first_node.next if self._validate_node(self._first_node) else None

        try:
            #while the next value is not None, we add "," and the value of the Node
            while current_node:
                final_list += ''.join(f',{str(current_node)}')

                #the next node is the next node of the last one
                current_node = current_node.next
        except:
            pass

        #finish the str of the stack
        return str(final_list) + ")"

def test_many_cases():
    s = Stack()

    # Teste para pilha vazia
    assert len(s) == 0
    assert s.pop() is None
    assert s.is_empty() == True

    # Adicionar e remover em uma pilha vazia
    s.push(1)
    assert len(s) == 1
    assert s.pop() == 1
    assert len(s) == 0

    # Adicionar e remover com diferentes tipos de dados
    s.push("string")
    s.push(3.14)
    s.push(True)
    assert len(s) == 3

    assert s._state == '__not_empty__'
    assert s.is_empty() == False

    assert s.pop() is True
    assert s.pop() == 3.14
    assert s.pop() == "string"
    assert len(s) == 0

    # Teste para adicionar muitos elementos
    for i in range(1000):
        s.push(i)
    assert len(s) == 1000

    # Teste para remover muitos elementos
    for i in range(999, -1, -1):
        assert s.pop() == i
    assert len(s) == 0

    # Teste para tentar remover de uma pilha vazia
    assert s.pop() is None

    # Teste para verificar se a pilha está vazia
    assert len(s) == 0

    assert s._state == "__empty__"

    print(s.peak())
    s.push('ooi')
    print(s.peak())
    s.push('nada')
    print(s.peak())
    s.push('aaa')
    print(s.peak())
    print(s)

test_many_cases()