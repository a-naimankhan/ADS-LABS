def bfs(graph):
    seen = set()
    path = []
    for n in g[v]:
        if n not in seen:
            path.append(n) 
        

#WORKS IN O(V+E) since we have to check all possible nodes 
#IF IT IS DIRECTRED GRAPH 

#IF IT IS UNDIRECTRED GRAPH WE JUST HAVE TO CHECK IF IT IS IN SEENT SET()


n = int(input())
g = [[] for _ in range(n)]

visited = [0] *n 


def dfs(v):
    visited[v] = 1 
    for u in g[v]:
        if visited[u] == 0:
            dfs
        if visited[u] == 1:
            print("cycle detected...")
        visited[u] = 2