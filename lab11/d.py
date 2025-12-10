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



n = int(input())
edges = []

mat = []
for _ in range(n):
    row = list(map(int , input().split()))
    mat.append(row)

for i in range(n):
    for j in range(i+1 , n):
        w = mat[i][j]
        edges.append((w , i+1 , j+1))

edges.sort()

dsu = DSU(n)
total = 0 
used = 0 


#kruskal
for w , u , v in edges:
    if dsu.unite(u , v):
        total += w 
        used += 1 
        if used == n-1:
            break

print(total)