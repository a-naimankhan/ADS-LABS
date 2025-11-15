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

    def insert(self, pos, x):
        new_node = Node(x)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        index = 0
        while curr and index < pos - 1:
            curr = curr.next
            index += 1

        if curr is None:
            print(-1)
            return

        new_node.next = curr.next
        curr.next = new_node

    def delete(self, pos):
        if self.head is None:
            print(-1)
            return

        if pos == 0:
            self.head = self.head.next
            return

        curr = self.head
        index = 0
        while curr.next and index < pos - 1:
            curr = curr.next
            index += 1

        if curr.next is None:
            print(-1)
            return

        curr.next = curr.next.next

    def print(self):
        if self.head is None:
            print(-1)
            return
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()
