    import heapq

def prim(n, g):
    visited = [False]*n
    pq = [(0, 0)]  # (weight, vertex)
    total = 0

    while pq:
        w, v = heapq.heappop(pq)
        if visited[v]: 
            continue
        visited[v] = True
        total += w

        for u, cost in g[v]:
            if not visited[u]:
                heapq.heappush(pq, (cost, u))

    return total
