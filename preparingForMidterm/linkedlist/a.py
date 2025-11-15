class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print(self):
        if self.head is None:
            print(-1)
            return
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()  # перенос строки

    def clear(self):
        self.head = None
