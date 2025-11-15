import heapq    

n , k = map(int , input().split())

nums = list(map(int , input().split()))

heap = []

for num in nums:
    heapq.heappush(heap , -num) 

    if len(heap) > k:
        heapq.heappop(heap)
    
    current = sorted([-x for x in heap])
    print(current)

for _ in range(n):
    if heap:
        print(-heap[0])
        heapq.heappop(heap)
    else:
        print(-1)