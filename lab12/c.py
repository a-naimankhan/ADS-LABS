import sys
input = sys.stdin.readline

INF = 10**15

class Edge:
    def __init__(self, a, b, cost):
        self.a = a
        self.b = b
        self.cost = cost


def find_negative_cycle(n, edges, start):
    d = [INF] * n
    p = [-1] * n
    d[start] = 0

    x = -1
    for _ in range(n):
        x = -1
        for edge in edges:
            if d[edge.a] < INF and d[edge.b] > d[edge.a] + edge.cost:
                d[edge.b] = max(-INF, d[edge.a] + edge.cost)
                p[edge.b] = edge.a
                x = edge.b

    if x == -1:
        return None

    y = x
    for _ in range(n):
        y = p[y]

    cycle = []
    cur = y
    while True:
        cycle.append(cur)
        cur = p[cur]
        if cur == y and len(cycle) > 1:
            break

    cycle.reverse()
    return cycle


n = int(input())
edges = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        edges.append(Edge(i, j, row[j]))

for v in range(n):
    cycle = find_negative_cycle(n, edges, v)
    if cycle is not None:
        print("YES")
        print(len(cycle))
        print(*[x + 1 for x in cycle])
        return

print("NO")

