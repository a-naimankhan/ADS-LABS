import sys
from collections import deque 
sys.setrecursionlimit(10 ** 7) 
input = sys.stdin.readline 



n , m = map(int , input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    x , y = map(int , input().split())
    g[x].append(y)
    g[y].append(x) 

visited = [False] * (n+1)
bigFam = 0 

def dfs_component(root):
    comp = []
    stack = [root]
    visited[root] = True 
    while stack:
        u = stack.pop() 
        comp.append(u)
        for v in g[u]:
            if not visited[v]:
                visited[v] = True 
                stack.append(v)
    return comp  

def build_tree_and_count(root , comp):
    parent = {root: -1}
    chiildren_count = {v:0 for v in comp}

    q = deque([root])
    visited2 = set([root])

    while q:
        u = q.popleft()
        for v in g[u]: 
            if v not in visited2:
                visited2.add(v)
                parent[v] = u
                chiildren_count[u] += 1 
                q.append(v) 

    return parent , chiildren_count 

answer = 0 

for i in range(1 , n+1):
    if not visited[i]:
        comp = dfs_component(i)

        root = min(comp)

        parent , children = build_tree_and_count(root , comp)

        for v in comp:
            if v == root:
                answer +=1  
            else:
                p = parent[v]
                if children[v] > children[p]:
                    answer += 1 
print(answer)