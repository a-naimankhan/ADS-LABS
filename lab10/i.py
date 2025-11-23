import sys 
input = sys.stdin.readline 
from collections import deque 

n , m = map(int , input().split())

g = [[] for _ in range(n+1)]
indeg = [0] * (n+1)

for _ in range(m):
    i , j = map(int , input().split())
    g[i].append(j)
    indeg[j] += 1 

q = deque() 
for i in range(1 , n+1):
    if indeg[i] == 0:
        q.append(i)

order = []

while q:
    u = q.popleft() 
    order.append(u)

    for v in g[u]:
        indeg[v] -= 1 
        if indeg[v] == 0:
            q.append(v) 

if len(order) == n:
    print("Possible")
    print(*order)
else:
    print("Impossible")