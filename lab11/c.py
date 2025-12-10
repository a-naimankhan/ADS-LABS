import sys 
input = sys.stdin.readline 

class DSU:
    def __init__(self , n):
        self.p = list(range(n+1))
        self.r = [0] * (n+1)

    def find(self , x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x 
    
    def unite(self , a , b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False 
        
        if self.r[a] < self.r[b]:
            a , b = b , a 
        self.p[b] = a  
        if self.r[a] == self.r[b]:
            self.r[a] += 1 
        return True 





n , m = map(int , input().split())
A ,B = map(int , input().split())

edges = []

for _ in range(m):
    parts = input().split()
    typ = parts[0]

    u = int(parts[1]) 
    v = int(parts[2]) 
    l = int(parts[3])

    if typ == "big":
        cost = l * A 
    elif typ == "small":
        cost = l * B 
    else:
        cost = l *min(A,B)

    edges.append((cost , u , v))

edges.sort() 
dsu = DSU(n)

total = 0 
used = 0 
for cost , u , v in edges:
    if dsu.unite(u , v):
        total += cost 
        used += 1 
        if used == n -1:
            break 
print(total)