import sys 
sys.setrecursionlimit(10**7)
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
            self.r[a] +=1  
        return True 
    

def make_next(n):
    return list(range(n+2))

def find_next(nxt , x):
    if nxt[x] == x:
        return x  
    nxt[x] = find_next(nxt , nxt[x])
    return nxt[x] 


n , m = map(int , input().split())
seg = []

for _ in range(m):
    l , r , c = map(int , input().split())
    seg.append((c , l , r))

seg.sort() 

dsu = DSU(n)
nxt = make_next(n)

ans = 0 

for c , l , r in seg:
    x = find_next(nxt , l)

    while x < r:
        y = x + 1  
        if dsu.unite(x , y):
            ans += c 
        
        nxt[x] = x + 1       
        x = find_next(nxt , x)

print(ans)
