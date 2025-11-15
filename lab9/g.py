def prefix_function(s):
    #pseudocode 
    n = len(s)
    pi = [0] * n 
    #for 1 , n :
        #j = pi[j-1]
        #while s[i] != prefix:
            #do smth with j pointer 
        #if they are equal 
            #j increase 
        #prefix = j 
    #return prefix  
    for i in range(1 , n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j 
    return pi 

s = input().strip() 
pi = prefix_function(s) 
n = len(s) 
p = n - pi[-1]
print(p)

