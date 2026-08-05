class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node

    def __init__(self):
        self.head = None

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

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            print("The Queue is empty")
            return None

        removed_data = self.head.data
        self.head = self.head.next

        return removed_data


q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()

print("DEQUEUE")
q.dequeue()
q.print_all()