from collections import deque 

def kill_mushrooms(grid):
    n = len(grid)
    m = len(grid[0])

    q = deque() 
    mushroms = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i ,j))
            elif grid[i][j] == 1:
                mushroms += 1 
            
    if mushroms == 0:
        return 0 
    

    dirs = [(1 , 0) , (-1 , 0) , (0,1) , (0 , -1)]
    minutes = -1 

    while q:
        size = len(q)
        minutes += 1 
    
        for _ in range(size):
            x , y = q.popleft()

            #do BFS
            for dx , dy in dirs:
                nx , ny = x + dx , y + dy 
                
                #check if dfs is able to go
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        mushroms -= 1 
                        q.append((nx , ny))

    if mushroms != 0:
            return -1
        
    return minutes 



n , m = map(int , input().split()) 
grid = []
for i in range(n):
    nums = list(map(int , input().split()))
    grid.append(nums)

print(kill_mushrooms(grid))