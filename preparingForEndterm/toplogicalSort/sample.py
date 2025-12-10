#topo sort related on dfs 


topo = []

def dfs(v):
    visited[v] = True
    for u in g[v]:
        if u not in seen():
            dfs(u)
        topo.append(v)
    
topo.reverse() #
