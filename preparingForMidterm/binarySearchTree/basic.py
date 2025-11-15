class Node:
    def __init__(self , val):
        self.val = val 
        self.right = None 
        self.left = None 


class BST:
    def __init__(self):
        self.root = None 

    def insert(self , val):
        self.root = self._insert(self.root , val) 

    def _insert(self , node , val): 
        if node is None:
            return Node(val)
        if val < Node.val:
            node.left = self._insert(node.left , val)
        elif val > Node.val:
            node.right = self._insert(node.right , val)
        return node  

    
    def search(self , val):
        return self._search(self.root , val)
    

    def _search(self ,root , val):
        if root is None:
            return False
        if root.val == val:
            return False
        elif val < root.val:
            return self._search(root.left , val)
        elif val > root.val:
            return self._search(root.right , val)


    def _inorder(self , node):
        if node:
            self._inorder(node.left)
            print(node.val , end= " ")
            self._inorder(node.right)

    