class Node:
    def __init__(self , x):
        self.val = x
        self.left = None
        self.right = None  


class BST:
    def __init__(self):
        self.root = None
    

    def insert(self , x):
        self.root = self._insert(self.root , x)

    def _insert(self , node , x):
        if node is None:
            return Node(x)
        
        if x < node.val:
            node.left = self._insert(node.left , x) 
        elif x > node.val:
            node.right = self._insert(node.right , x) 
        
        return node  
    
    def count_leaves(self , node):
        if node is None:
            return 0 
        if node.left is None and node.right is None:
            return 1 
        return self.count_leaves(node.left) + self.count_leaves(node.right)


n = int(input())
nums = list(map(int , input().split()))

tree = BST() 
for x in nums:
    tree.insert(x)
    
print(tree.count_leaves(tree.root))
