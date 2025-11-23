from collections import deque

#Построй adjacency list

#Выполни BFS начиная с вершины 0

#Запиши порядок обхода

#Определи сколько ребер в графе

#Определи степень (degree) каждой вершины

adjencylist = {}

n = int(input())
matrix = [[]]

for i in range(n):
    for j in range(n):
        num = int(input())
        matrix[i][j] = num 

#пройтись по массиву что бы теперь записать все в эйдженси лист 

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            #adjencylist[i] = #inserting this data 


#once I have everything 
def bfs(graph , start):
    visited = set() 
    q = deque([start])
    visited.add(start)

    order = []
    counter = 0 
    while q:
        node = q.popleft() 
        order.append(node)

        for nei in graph[node]:
            if node not in visited:
                visited.add(node)
                order.append(node)
                counter += 1 
                print(nei , end="->") 
                print(f"degree of {node} is {len(graph[node])}")            

    print(counter + 1 )      
    return order #вот поидее то как пройдется бфс 
            