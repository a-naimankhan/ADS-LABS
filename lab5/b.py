class MaxHeap:
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
            if self.data[i] > self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break 

    def _heapify_down(self, i):
        n = len(self.data)
        while True:
            left = 2 * i + 1 
            right = 2 * i + 2 
            largest = i 

            if left < n and self.data[left] > self.data[largest]:
                largest = left
            if right < n and self.data[right] > self.data[largest]:
                largest = right
            
            if largest == i:
                break
        
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest 


heap = MaxHeap()
n = int(input())
nums = list(map(int, input().split()))

for x in nums:
    heap.push(x)

while len(heap) > 1:
    y = heap.pop()
    x = heap.pop()

    if x != y:
        heap.push(y - x)

print(heap.pop() if len(heap) else 0)