from collections import deque 

n = int(input())
nums = list(map(int , input().split()))

dq = deque(range(1 , n+1))

possible = True
for num in nums:
    if not dq:
        possible = False
        break

    if dq[0] == num:
        dq.popleft()
    elif dq[-1] == num:
        dq.pop()
    else:
        possible = False
        break

print("YES" if possible else "NO")