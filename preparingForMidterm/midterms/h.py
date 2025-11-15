class Node:
    def __init__(self , val):
        self.val = val 
        self.left = None
        self.right = None 
    

class BST():
    def __init__(self):
        self.root = None 
    
    def insert(self ,x):
        self.root = self._insert(self.root, x) 

    def _insert(self , node , x):
        if node is None:
            return Node(x)
        
        if x < node.val:
            node.left = self._insert(node.left , x)
        elif x > node.val:
            node.right = self._insert(node.right , x)
        return node
    
    def find_max_depth(self , node):
        if node is None:
            return 0 

        left_depth = self.find_max_depth(node.left)
        right_depth = self.find_max_depth(node.right)
        return max(left_depth , right_depth) + 1
        
