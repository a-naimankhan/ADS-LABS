class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_back(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop_front(self):
        if self.head is None:
            print(-1)
            return
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        print(val)

    def pop_back(self):
        if self.tail is None:
            print(-1)
            return
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        print(val)

    def reverse(self):
        if self.head is None:
            return
        curr = self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev  # потому что ссылки уже поменялись
        # после цикла head и tail нужно свапнуть
        self.head, self.tail = self.tail, self.head

    def print_forward(self):
        if self.head is None:
            print(-1)
            return
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    def print_backward(self):
        if self.tail is None:
            print(-1)
            return
        curr = self.tail
        while curr:
            print(curr.val, end=" ")
            curr = curr.prev
        print()
