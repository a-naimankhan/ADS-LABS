import heapq 
import sys 

input = sys.stdin.readline 
#MinHeapq
n , m = map(int , input().split())
nums = list(map(int , input().split()))

heapq.heapify(nums)
operations = 0 

while nums and nums[0] < m: 
    if len(nums) < 2:
        print(-1)
        break 

    least = heapq.heappop(nums)
    second = heapq.heappop(nums)
    
    new = least + 2 * second 
    heapq.heappush(nums , new)
    operations +=1  
else:
    print(operations)