#this algorithm который считывает кратчайшие пути между всеми парами 

#works if the graph is less than < 500 vertices and can store n*n matrix 


#улучшение пути от i-j используя промежуточную вершину к 
dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])


#pseudocode 
#for k in range(n):
    #for i in range(n):
        #for j in range(n):
            #dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])

    
def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
