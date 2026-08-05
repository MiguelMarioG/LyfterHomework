class Node:
    def __init__(self, data: str, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    head: Node
    tail: Node


    def __init__(self):
        self.head = None
        self.tail = None


    def print_forward(self):
        current_node = self.head

        if current_node is None:
            print("The Double Linked List is empty")
            return

        print("Forward:  ", end="")
        while current_node is not None:
            if current_node.next is not None:
                print(current_node.data, end=" -> ")
            else:
                print(current_node.data)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail

        if current_node is None:
            print("The Double Linked List is empty")
            return

        print("Backward: ", end="")
        while current_node is not None:
            if current_node.prev is not None:
                print(current_node.data, end=" <- ")
            else:
                print(current_node.data)
            current_node = current_node.prev


    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def delete(self, data):
        current_node = self.head

        while current_node is not None and current_node.data != data:
            current_node = current_node.next

        if current_node == self.head:
            self.head = current_node.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

        elif current_node == self.tail:
            self.tail = current_node.prev
            self.tail.next = None

        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev


dll = DoubleLinkedList()

dll.append("A")  
dll.append("B")
dll.append("C")
dll.print_forward()
dll.print_backward()
print()
dll.prepend("X")
dll.print_forward()
dll.print_backward()
print()
dll.delete("B")
dll.print_forward()
dll.print_backward()
print()
dll.print_forward()
dll.print_backward()


