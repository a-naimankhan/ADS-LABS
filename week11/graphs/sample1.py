#adjacency list 
#is when it's constuctucted by map 
#it's memory complextiy is O(V+E)
#Matrix type where row is a key and collumn is does it havea connection 
#Edge list where is saved as [from , To] and 2*V number of tuples  



#convert matrix into a adjency list 
#pseudocode 

#Al := make(map[int][]int{})
#for row , val := range matrix {
    #paths := []int{}
    #for col , val := range matrix[row] {
        #if matrix[row][col]  {
        #  Al[i].pushback(j) 
#}
#}
#}


#pseudocode of DFS  in graph in adjency list 
def bFS(m[int][]int{}) { 
    q := queue<int>
    q.append(q, map[0])
    seen := make(map[int]bool)
    seen[currentNode] = True
    for len(q) > 0{
        currentNode = q.front()
        
        q.pop() 
        for _ , num := range M[currentNode] {
            if  !seen[num]{
                q.push(num)
            }
            
        }
    } 
}