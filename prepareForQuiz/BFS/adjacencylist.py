from collections import deque 

def bfs(graph , start):
    visited = set() 
    q = deque([start])
    visited.add(start)

    order = []

    while q:
        node = q.popleft() 
        order.append(node)

        for neighobr in graph[node]:
            if neighobr not in visited:
                visited.add(neighobr)
                q.append(neighobr)
    return order

#O(V+E)  

#BFS recursive 
def bfs_recursive(graph , queue , visited , order):
    if not queue:
        return 
    
    node = queue.popleft() 
    order.append(node) 

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            order.append(nei) 
        
    bfs_recursive(graph , queue , visited , order)

#Adjacency list is dictionary or map with key as Vertex and values as its neghours 
#can work in both directed undirected graph 
#with such keys when graph is disconnected the m[k] = null  
#it is compact to save but expensive to check the connections 


graph = {
    0: [1,2] , 
    1: [0,3] ,
    2: [0] , 
    3: [1] 
}

#Adjency matrix is two d arra where rows is keys and collumns is the neighbours and if row and collumn has connection the a[row][column] = 1 
#it is easy to check conections since it's O(1) but saving is O(n^2)

matrix = [
    [0 , 1 , 1 , 0] , 
    [1 , 0 , 0 , 1] , 
    [1 , 0 , 0 , 0] , 
    [0 , 1 , 0 , 0]
]


#hash tables Average complexity 
#insert O(1)  , Search O(1) , worst case: O(n) 