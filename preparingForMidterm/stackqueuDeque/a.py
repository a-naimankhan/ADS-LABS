class stack:
    def __init__(self):
        self.items = []


    def is_empty(s):
        return s.items == [] 

    def push(self , item):
        self.items.append(item) 
    
    def pop(self):
        if len(self.items) == 0:
            raise IndexError 

        self.items.pop()
    
    def top(self):
        if len(self.items) == 0:
            raise IndexError 

        curr = self.items[-1]
        return curr 
    
n = int(input())
s = stack() 
for _ in range(n):
    command = input().split() 

    if command[0] == "push":
        s.push(int(command[1])) 
    elif command[0] == "pop":
        s.pop()
    elif command[0] == "top":
        print(s.top()) 
    