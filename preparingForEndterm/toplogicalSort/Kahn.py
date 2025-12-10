from collections import deque

indegree = [0]*n
for v in range(n):
    for u in g[v]:
        indegree[u] += 1

q = deque([v for v in range(n) if indegree[v] == 0])
order = []

while q:
    v = q.popleft()
    order.append(v)
    for u in g[v]:
        indegree[u] -= 1
        if indegree[u] == 0:
            q.append(u)

print(order)
