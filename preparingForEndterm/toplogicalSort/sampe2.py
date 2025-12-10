visited = [False] * n 
order = []


def dfs(v):
    visited[v] = True
    for u in g[v]:
        if not in visited[u]:
            dfs(u)
        order.append(v)

for i in range(n):
    if not visited[v]:
        dfs(i)

order.reverse()
print(order)