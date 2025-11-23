from collections import deque 

n , m = map(int , input().split())
grid = [list(map(int , input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dirs = [(1 ,0 ) , (-1 , 0) , (0 , 1) , (0 , -1)]

def bfs(x ,y):
    q = deque() 
    q.append((x,y))
    visited[x][y] = True 

    while q:
        cx , cy = q.popleft() 
        for dx , dy in dirs:
            nx , ny = cx+dx , cy + dy 
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == "1":
                    visited[nx][ny] = True 
                    q.append((nx , ny))

count = 0 
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1' and not visited[i][j]:
            bfs(i , j)
            count +=1 

print(count) 

#idea такая типо раз мы нашли участок где 1 делаем бфс и добавляем в визитед 
#и при некст итерейшн уже все что прошло через тоесть единички стали тру мы идем до некст 1 которая виситед[posx][posy] = false  
