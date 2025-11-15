def prefix_function(s):
    n  = len(s) 
    pi = [0] * n 

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


used = [False] * (n+1)
for i in range(n - 1):
    used[pi[i]] = True


count = 0 
length = pi[-1]

if length == 0:
    length = pi[n-2]

while length > 0:
    if used[length]: #будто бы здесь фолс идет  
        count += 1
    length = pi[length - 1] 

if count == 0:
    length = pi[n - 2]
    while length > 0:
        if used[length]:
            count += 1
        length = pi[length - 1]

print(count)
