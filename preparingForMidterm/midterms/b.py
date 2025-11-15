import heapq
n , k = map(int , input().split())

nums = list(map(int , input().split()))

heap = []

for i in range(n):
    num = nums[i]
    heapq.heappush(heap , num)
    if len(heap) > k:
        heapq.heappop(heap)
    if len(heap) < k:
        print("Bonucci")
    else:
        print(heap[0])
        


