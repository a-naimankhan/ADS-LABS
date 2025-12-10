class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True



def kruskal(n, edges):
    edges.sort()  # сортируем по весу
    dsu = DSU(n)
    mst = []
    total = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w

    return total, mst
