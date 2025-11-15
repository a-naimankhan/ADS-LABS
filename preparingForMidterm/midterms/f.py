import heapq 

def find_med(l , r):
    return (l+r) // 2 

n = int(input())
nums = list(map(int , input().split()))

min_heap = []
max_heap = []

for num in nums:
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap , num)
    else:
        heapq.heappush(min_heap , num)

    
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap , -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap , heapq.heappop(min_heap))

    if len(max_heap) == len(min_heap):
        median = (-max_heap[0] + min_heap[0]) // 2 
    else:
        median = -max_heap[0] 

    if median == int(median):
        print(int(median))
    else:
        print(median)