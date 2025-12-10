import sys
input = sys.stdin.readline

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
order = list(map(lambda x: int(x) - 1, input().split()))

dist = [row[:] for row in adj]

active = [False] * n
answer = []
order_rev = order[::-1]

for k in order_rev:
    active[k] = True

    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    max_val = 0
    for i in order_rev:
        if not active[i]: continue
        for j in order_rev:
            if active[j]:
                max_val = max(max_val, dist[i][j])

    answer.append(max_val)

for el in answer:
    print(el)
