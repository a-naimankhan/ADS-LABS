class Node:
    def __init__(self , val):
        self.val = val 
        self.right = None
        self.left = None  

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self , v):
        self.root = self._insert(self.root , v)

    def _insert(self , node ,  val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left , val)
        elif val > node.val:
            node.right = self._insert(node.right , val)
        return node 

    def search(self , target):
        return self._search(self.root , target)

    def _search(self , node , target):
        if node is None:
            return False
        if node.val == target:
            return True
        elif target < node.val:
            return self._search(node.left , target)
        elif target > node.val:
            return self._search(node.right , target)
        
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self , node):
        if node:
            self._inorder(node.left)
            print(node.val , end=" ")
            self._inorder(node.right)


tree = BST() 

while True:
    cmd = input().split()
    if cmd[0] == "insert":
        tree.insert(int(cmd[1]))
    elif cmd[0] == "search":
        tree.search(int(cmd[1]))
        if tree.search(int(cmd[1])):
            print("FOUND")
        else:
            print("NOT FOUND")
    elif cmd[0] == "print":
        tree.inorder()
    elif cmd[0] == "exit":
        break          
        