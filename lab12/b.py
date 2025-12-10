import sys
import heapq
input = sys.stdin.readline

INF = 10**15

def dijkstra(start, graph, n):
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)
        if d != dist[v]:
            continue

        for to, w in graph[v]:
            if dist[to] > d + w:
                dist[to] = d + w
                heapq.heappush(pq, (dist[to], to))

    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    l, r, w = map(int, input().split())
    l -= 1
    r -= 1
    graph[l].append((r, w))
    graph[r].append((l, w))

s, a, b, f = map(int, input().split())
s -= 1
a -= 1
b -= 1
f -= 1

d1 = dijkstra(s, graph, n)
d2 = dijkstra(a, graph, n)
d3 = dijkstra(b, graph, n)

if d1[a] >= INF or d2[b] >= INF or d3[f] >= INF:
    print(-1)
    

path1 = d1[a] + d2[b] + d3[f]
path2 = d1[b] + d3[a] + d2[f]

print(min(path1, path2))


