import sys 
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline 

n , m = map(int , input().split())
g = [[] for _ in range(n+1)]
edges = []

for _ in range(m):
    u , v = map(int , input().split())
    g[u].append(v)
    edges.append((u , v)) 

WHITE = 0 
GRAY = 1 
BLACK = 2 

color = [WHITE] * (n+1)
parent = [-1] * (n+1)
cycle = []

def dfs(u):
    global cycle 
    color[u] = GRAY 
    for v in g[u]:
        if color[v] == WHITE:
            parent[v] = u 
            if dfs(v):
                return True 
        elif color[v] == GRAY:
            x = u 
            cycle = [(u , v)]
            while x != v:
                px = parent[x]
                cycle.append((px , x))
                x = px 
            return True 
    color[u] = BLACK 
    return False 

found = False 
for i in range(1 , n+1):
    if color[i] == WHITE and dfs(i):
        found = True
        break 

if not found:
    print("YES")
    exit()  
else:
    print("NO")
