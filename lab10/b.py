from collections import deque 

def find_shortest_path(matrix , s , e):
    start , end = s-1 , e-1  
    n = len(matrix)
    #pseudocode 
    q = deque() 
    visited = [False] * n 
    dist = [-1] * n 

    q.append(start)
    visited[start] = True  
    dist[start]= 0  

    while q:
        u = q.popleft() 

        if u == end:
            return dist[u]

        for v in range(n):
            if matrix[u][v] == 1 and not visited[v]:
                visited[v] = True 
                dist[v] = dist[u] + 1 
                q.append(v) 
    
    return -1 

   



n = int(input().strip())
grid = []

for i in range(n):
    nums = list(map(int , input().split()))
    grid.append(nums)

start , end = map(int , input().split()) 
print(find_shortest_path(grid , start , end))
