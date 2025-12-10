def dfs(v):
    visited[v] = True
    comp.append(v)
    for u in g[v]:
        if not visited[v]:
            visited.append(v)


for i in range(n):
    if not visited[v]:
        comp = []
        dfs(i)
        print("component : " , i)