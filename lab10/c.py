from collections import deque

def number_of_operations(start , end):
      
    #pseudocode 
    #while :
        #start *= 2 
        #then another checkment if start more or not 
        #if it less start =- 1
        # and every time in cycle check if it's equal  
        #if start + 1 == end: 
            #start += 1  
    #naah butdto by BFS a ne greedy 
    #bfs + backtracking 
    #dist = {}
    #parent = {}

    #q 

    #q[start]
    #distance[start] ... 

    #while q:
        #x = q.pop 
        #if x == end:
            #return dist[x] 

        #if x*2 not in parent and not in dist:
        #   dist 
        # 
        # if x -1 is able and not in dist 

    dist = {}
    parent = {}

    q = deque() 
    
    q.append(start) 
    dist[start] = 0 
    parent[start] = None 

    while q:
        x = q.popleft() 

        if x == end:
            break 
        

        if x * 2 < 10000 and (x*2) not in dist:
            dist[x*2] = dist[x] + 1  
            parent[x*2] = x  
            q.append(x*2)
        
        if x - 1 >= 1 and (x - 1) not in dist:
            dist[x-1] = dist[x] + 1 
            parent[x-1] = x 
            q.append(x-1) 
    
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse() 
    return dist[end] , path 

start , end = map(int , input().split())
steps , path = number_of_operations(start , end)
path = path[1:]
print(steps)
print(*path)