
#task 1  
for i in range(1 , len(pattern)-1):
    while j > 0 and p[i] != p[j]:
        j = lps[j-1]
    if p[i] == p[j]:
        j += 1  
        lps[i] = j  

#task 2:
p = "ababaca"
lps = [0 , 0 , 1 , 2 , 1 , 0 , 1] 

#task 3 : 
cur_hash = (cur_hash - left * p **(len(pattern) - 1)) % mod
cur_hash = (cur_hash * p + ord(c) ) % mod  

#task 4:
cur_hash = (cur_hash + p + ord(c)) % mod  

#task 5:
0: [1,2]
1: [3]
2: [4]
3: []
4: [5]
5: []

BFS = [0 , 1 , 3 , 2 , 4 , 5 ] 
#task 6
DFS = [0 , 1 , 2 , 3 , 4 , 5] 

#task 7 
   0 1 2 3
0 [0 1 0 1]
1 [1 0 1 0]
2 [0 1 0 1]
3 [1 0 1 0]

adjency = {
    0: [1 , 3] ,
    1: [0 , 2] ,
    2: [1 , 3] , 
    3: [0 , 2]
}

#task 8
# 4? typo 8 // 2 = 4 

#task 9 
#a) BFS adjacency list
#b) BFS adjacency matrix
#c) KMP worst-case
#d) Rabin–Karp worst-case
# ans: 
# a)O(V+E)
# b)O(V^2)
# c)O(n+m)
# d)O(nm) 
#
# task 10 
# adjency matrix    

