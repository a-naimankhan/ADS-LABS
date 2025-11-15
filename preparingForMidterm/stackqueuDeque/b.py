class queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0 
    
    def push(self , x):
        return self.items.append(x)

    def pop(self):
        if self.is_empty():
            print(-1)
        self.items.pop()

    def front(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.items[0])
    
    def back(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.items[-1])
    
    def size(self):
        return len(self.items)

    def clear(self):
        if self.is_empty:
            print(-1)
        else: 
            while self.items:
                self.items.pop()
        
q = queue()
while True:
    command = input().split()
    if command[0] == "push":
        q.push(int(command[1]))
    elif command[0] == "pop":
        q.pop()
    elif command[0] == "front":
        q.front()
    elif command[0] == "back":
        q.back()
    elif command[0] == "size":
        print(q.size()) 
    elif command[0] == "clear":
        q.clear()
    elif command[0] == "exit":
        break
    
