n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]

rows.sort(key = lambda x: [-sum(x) , x])

for row in rows:
    print(*row , end= " \n")
print()
