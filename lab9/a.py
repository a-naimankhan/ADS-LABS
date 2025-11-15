def min_repetion(A , B):
    repeated = A 
    count = 1 

    while len(repeated) < len(B):
        repeated += A 
        count += 1 
    
    if B in repeated:
        return count 
    elif B in (repeated + A):
        return count + 1 
    else:
        return -1 


s = input() 
subS = input() 
print(min_repetion(s , subS))
#pseudocode 
#if strings.ContainAny(s , subs){
        #return counter 
    #} 
    #else:
        #s += s 
        #counter++ 