import heapq
import sys 
input = sys.stdin.readline 
#MaxHeapq
n , x = map(int , input().split())
rows = list(map(int , input().split()))

heap = [-r for r in rows]
heapq.heapify(heap)

total = 0 

for _ in range(x):
    if not heap:
        break 
    curr = -heapq.heappop(heap)
    total += curr 
    curr -= 1  
    if curr > 0:
        heapq.heappush(heap , -curr)

print(total)