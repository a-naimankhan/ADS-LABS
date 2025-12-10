
#Собрать все рёбра

#Отсортировать по весу
#Идти по рёбрам:


#если объединяет две разные компоненты → берём

#иначе → пропускаем (иначе цикл)

#Используем DSU (Union-Find).


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])  # path compression
        return self.parent[v]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False  # cycle
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

def kruskal(n, edges):
    # edges: [(w, u, v)]
    edges.sort()
    dsu = DSU(n)
    mst = []
    total = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w

    return total, mst
