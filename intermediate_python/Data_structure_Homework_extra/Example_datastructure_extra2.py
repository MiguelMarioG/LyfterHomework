class Node:
    def __init__(self, data: str, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    head: Node
    tail: Node


    def __init__(self):
        self.head = None
        self.tail = None


    def print_all(self):
        current_node = self.head

        if current_node is None:
            print("the Queue is empty")
            return

        while current_node is not None:
            if current_node.next is not None:
                print(current_node.data, end= " -> ")
            else:
                print(current_node.data)
            current_node = current_node.next


    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_back(self, data):
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

        if current_node is None:
            return

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


ll = LinkedList()

ll.insert_front(10)  
ll.insert_front(20)
ll.print_all()

ll.insert_back(30)
ll.print_all()

ll.delete(10)
ll.print_all()

