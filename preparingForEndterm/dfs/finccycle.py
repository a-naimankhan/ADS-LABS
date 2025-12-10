WHITE , GRAY , BLACK = 0 , 1 , 2 # to check the состояние граф ноуда 
color = [n] * WHITE

cycle_found = False #flag 


#sam dfs in directed graph  
def dfs(v):
    global cycle_found 
    color[v] = GRAY
    for u in g[v]:
        if color[v] == WHITE:
            dfs(v) #if color is still didn't checked we recursively ask again 
        elif color[v] == GRAY:
            cycle_found = True
        color[v] #so we put the last checked element as found and have the value where cycle end

#if it is undirected it works with two paremetrs vertex and parennt 
def dfs_undirected(v , parent):
    for u in graph[v]:
        if u == parent:
            continue
        if visited[v]:
            print("found") #then break or escape from the loop 
        else:
            dfs_undirected(u , v)
