#Topological sort is one of the type that works with graph 
#works only in directional graphs 
#ABKCDEF 
#a -> b -> D-> E 
    #D -> F E -> F 
#ну короче граф сверху и снизу который конектиться между собой то что стоит паррарельно и в конце стоит Е  

#проходя через DFS получается 
#ABDEFCKH 
#doesn't work( have to modify  


#pseudocode 
#def DFS(G):
    #seen = set()
    #ans = []
    #for element in G:
        #if element not in SEEN:
            #DFS_rec(G , )


#def DFS_rec(next , ):
    #ans.append(next)
    #for element in G[next]:
        #if element not in seen:
            #DFS_rec(e , G)

    #ans.append(next)

#after everything is done I have to reverse it so I'll have a sorted one 
 


#the second scenario 

#more BFS likely 
#AKHBDCEF 
#Topological_Sort(G):
    #hm := make(map[int]int)
    #q := queue() 
    #for element in G:
        #for e in item[element]:
            #d[e]++  

    #for keys , val := range hm{
        #if val == 0 {
            #q.push(val)
            #..... 
            # have to continue 
            # but no time( 
            #    
# }    
#}

#for len(q) > 0 {
    #c := q[0]
    #q.pop() 
    # for _ , el  := range G[c]{
        #d[el]-- 
        #q = append(q , el) 
# }    
#}