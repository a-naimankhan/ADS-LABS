import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.p = list(range(n+1))
        self.r = [0] * (n+1)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True


def solve():
    n, m = map(int, input().split())

    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    dsu = DSU(n)
    
    active = [False] * (n+1)
    comp = 0
    ans = [0] * (n+1)

    for cur in range(n, 0, -1):
        active[cur] = True
        comp += 1  

        for v in g[cur]:
            if active[v]:
                if dsu.unite(cur, v):
                    comp -= 1

        ans[cur] = comp

    for i in range(1, n+1):
        print(ans[i+1])
    print(0)

solve()
