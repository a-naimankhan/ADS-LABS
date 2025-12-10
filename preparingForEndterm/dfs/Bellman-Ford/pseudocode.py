#Повторяй релаксацию рёбер так долго, пока пути улучшаются 
#pseudocode 
#dist[s] = 0 
#dist[others] = inf 

#repeat V-1 times:
#    for each edge (u , v , w):
#        if dist[v] > dist[u] + w:
#           dist[v] = dist[u] + w  


def bellman_ford(n , edges , start):
    INF = 10 ** 15 
    dist = [INF] * n 
    dist[start] = 0 

    for _ in range(n-1):
        changed = False
        for u , v , w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w 
                changed = True
        if not changed:
            break 

    for u , v , w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            return None , True
    
    return dist , False 


n = int(input()) #количество вершин 
edges = [[] for _ in range(n)] #количество ребер 
start = int(input()) #startpoint

