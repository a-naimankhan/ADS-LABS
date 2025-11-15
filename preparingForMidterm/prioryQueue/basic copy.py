import heapq 
#maxheap
heap = []

while True:
    cmd = input().split()
    if cmd[0] == "push":
        heapq.heappush(heap , -int(cmd[1]))
    elif cmd[0] == "pop":
        if heap:
            heapq.heappop(heap)
        else:
            print(-1)
    elif cmd[0] == "top":
        if heap:
            print(-heap[0])
        else:
            print(-1)
    elif cmd[0] == "exit":
        break 

