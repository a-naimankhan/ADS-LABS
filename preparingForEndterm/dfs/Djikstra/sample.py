import heapq

def dijkstra(n, g, start):
    INF = 10**18
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]  # (distance, vertex)

    while pq:
        d, v = heapq.heappop(pq)
        if d != dist[v]:
            continue
        for u, w in g[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                heapq.heappush(pq, (dist[u], u))

    return dist



def dijkstra_no_heap(n, g, start):
    INF = 10**15
    dist = [INF] * n
    used = [False] * n

    dist[start] = 0

    for _ in range(n):
        # ищем вершину с минимальным dist
        v = -1
        for i in range(n):
            if not used[i] and (v == -1 or dist[i] < dist[v]):
                v = i

        used[v] = True
        
        for u, w in g[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w

    return dist
