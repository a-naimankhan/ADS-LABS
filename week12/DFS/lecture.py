#pseudocde 

#DFS(G):
#    G = [A:[B]
#    B:[A,C,D]
#    C:[B . F , R]]
#    seen = set()
#
#    for element in G:
#        if element not in seen:
#            return #chto to ne cheknuto case when graph is disconnected 
#        
#    DFS_REC(G , S , V)     


#DEF_REC(G , next_ , V):
#    seen.add(next_)
#
#    if G[next_] not in seen:
#        for el in G[next_]:
#            DFS_REC(G , el , V)  

#TIME COMPLEXITY O(V+E)
#SPACE COMPLEXITY O(V+E)


#iterative 
#DFS_helper(G , stack ):
#    while !stack:
#        c = st.pop() 
#        st.pop() 
#        v.insert(c)
#        for neighbour in G[c]:
#            if neighbour not seen:
#                st.push(c)
            
#HUI EGO CHTO TYT PROISHODIT VOOBSHE 


#правильный псевдокод  
#рекурснивная версия  

#DFS(G):
#    seen = set()
#    for node in G:
#        if node not in seen:
#            DFS_rec(node)

#DFS_rec(node):
#    seen.add(node)
#    for neigh in G[node]:
#        if neigh not in seen:
#            DFS_rec(neigh) 



#iterative way : 
#DFS_helper(G , stack ):
#    while !stack:
#        c = st.pop() 
#        st.pop() 
#        v.insert(c)
#        for neighbour in G[c]:
#            if neighbour not seen:
#                st.push(c) 




