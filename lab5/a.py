import sys 
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def push(self, val):
        self.data.append(val)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def _heapify_down(self, i):
        n = len(self.data)
        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == i:
                break

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest


n = int(input())
arr = list(map(int, input().split()))

heap = MinHeap()
for x in arr:
    heap.push(x)

total_cost = 0

while len(heap) > 1:
    a = heap.pop()
    b = heap.pop()

    if a is None or b is None:
        break

    s = a + b
    total_cost += s
    heap.push(s)

print(total_cost)