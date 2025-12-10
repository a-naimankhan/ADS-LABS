import sys
input = sys.stdin.readline

INF = 2000000007

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if (a ^ b) & 1:
            a, b = b, a
        self.parent[b] = a
        return True


def find_min_radius(left, right, n, x, y):
    min_radius = 0

    while left <= right:
        mid = (left + right) // 2

        dsu = DSU(n)

        for i in range(1, n + 1):
            xi, yi = x[i], y[i]
