import sys 
sys.setrecursionlimit(10**7)
input = sys.stdin.readline 

n , m = map(int , input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    x , y = map(int , input().split())
    g[x].append(y)
    g[y].append(x)
fake_input = input().strip() 
s , f = map(int , input().split())

visited = [False] * (n+1)

def dfs(u):
    visited[u] = False
    for v in g[u]:
        if not visited[v]:
            dfs(v)

dfs(s)

print("YES" if visited[f] else "NO")

