class Node:
    def __init__(self, data: str, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleEndedQueue:
    head: Node
    tail: Node


    def __init__(self):
        self.head = None
        self.tail = None


    def print_structure(self):
        current_node = self.head

        if current_node is None:
            print("the Queue is empty")
            return

        while current_node is not None:
            if current_node.next is not None:
                print(current_node.data, end= "<->")
            else:
                print(current_node.data)
            current_node = current_node.next


    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def pop_left(self):
        if self.head is None:
            print("The deque is empty; POP_LEFT cannot be performed")
            return None

        popped = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        popped.next = None 
        return popped.data

    def pop_right(self):
        if self.tail is None:
            print("The deque is empty; POP_RIGHT cannot be performed.")
            return None

        popped = self.tail
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        popped.prev = None 
        return popped.data


deque = DoubleEndedQueue()

first_node = Node("Hello")
second_node = Node("World")
third_node = Node("third")
fourth_node = Node("fourth")

deque.push_right(first_node)  
deque.push_right(second_node) 
deque.push_left(third_node)
deque.push_right(fourth_node)    

deque.print_structure()

print("\nPopped Right:", deque.pop_right()) 
print("Popped Left:", deque.pop_left())   

print("\nFinal Structure:")
deque.print_structure()