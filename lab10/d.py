from collections import deque
import math  
import sys 
input = sys.stdin.readline 

inf = 10 ** 5 

#def change_red(v):
    #pseudocode 
    #save n
    #change n  into red 
    #save its possition
    #q = deque()  
    #dist = [inf] *(v+1)
    #if dist[v] > 0:
    #    dist[v] = 0 
    #    bfs_update()


#def print_nearest(n int):
    #pseudocode 
    #BFS to find nearest
    #print it 
    #q = deque() 
    #start 
    #... 


n , m , q = map(int , input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a , b = map(int , input().split()) 
    g[a].append(b)
    g[b].append(a) 

INF = 10 ** 18  
dist = [INF] * (n+1)

queue = deque() 

def bfs_update():
    while queue:
        u = queue.popleft() 
        for w in g[u]:
            if dist[w] > dist[u] + 1:
                dist[w] = dist[u] + 1 
                queue.append(w) 

for _ in range(q):
    t , v = map(int , input().split())

    if t == 1:
        if dist[v] > 0:
            dist[v] = 0 
            queue.append(v) 
            bfs_update() 

    else:
        if dist[v] == INF:
            print(-1)
        else:
            print(dist[v])