import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

total_cost = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    s = a + b
    total_cost += s

    heapq.heappush(arr, s)

print(total_cost)