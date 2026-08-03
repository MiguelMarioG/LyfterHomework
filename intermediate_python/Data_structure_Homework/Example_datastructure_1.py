class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is not None:
            popped = self.head
            self.head = self.head.next  
            return popped.data
        else:
            print("The stack is empty; POP cannot be performed")
            return None


first_node = Node("Hello")
my_stack = Stack(first_node)

second_node = Node("World")
my_stack.push(second_node)

third_node = Node("third")
my_stack.push(third_node)

forth = Node("forth")
my_stack.push(forth)

my_stack.print_structure()

print()
print("POP")

my_stack.pop()
my_stack.print_structure()

print()
print("POP")

my_stack.pop()
my_stack.print_structure()

print()
print("POP")

my_stack.pop()
my_stack.print_structure()

print()
print("POP")

my_stack.pop()
my_stack.print_structure()