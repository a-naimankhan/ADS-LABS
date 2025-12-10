#bfs версия идем до того момента пока у вершин уже не будет дальше куда идти 

from collections import deque 

def topo_sort_kahn(n , graph):
    index = [0] * n 
    for u in range(n):
        for v in graph[u]:
            index[v] +=1 

    
    q = deque([u for u in range(n) if index[u] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] = -1 
            if indeg == 0:
                q.append(v)

    
    if len(order) != n:
        return None 


    return order 

#dfs version мы идем до конца пока не залутает конечно и только потом добавляем в стэк 

def topo_sort_dfs(n , graph):
    visited = [0] * n 
    order = []

    def dfs(u):
        if visited[u] == 1:
            return False
        if visited[u] == 2:
            return True
        visited[u] = 1
        for v in graph[u]:
            if not dfs(v):
                return False 
        visited[u] = 2
        order.append(u)
        return True 

    for i in range(n):
        if visited[i] == 0:
            if not dfs(i):
                return None
    
    return order[::-1]