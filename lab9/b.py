def count_occurences(s , T):
    count = 0 
    pos = T.find(s) 
    while pos != -1:
        count += 1 
        pos = T.find(s , pos + 1)
    return count 


s , k = input().split()
k = int(k)

T = input().strip()  


if count_occurences(s ,T) >= k:
    print("YES")
else:
    print("NO")

#pseudocode 
#maybe built-in funcs ? 
#pos = T.find(sbustr)
#while pos found 
    #counter++ 
    #and start searching from next pos 
#return counter 
#and check if it's >= k 