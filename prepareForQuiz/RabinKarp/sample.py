def rabin_karp(s , pattern):
    n , m = len(s) , len(pattern)

    if m > n:
        return []
    
    p = 31 
    mod = 10 ** 9 + 9 

    #hash of pattern
    pat_hash = 0 
    for c in pattern:
        pat_hash = (pat_hash * p + ord(c)) % mod 

    #hash(first_window)
    cur_hash = 0 
    for c in s[:m]:
        cur_hash = (cur_hash * p + ord(c)) % mod 

    #p^(m-1)
    power = pow(p , m-1 , mod) 

    res = []
    for i in range(n-m+1):
        if cur_hash == pat_hash:
            if s[i:i+m] == pattern:
                res.append(i) 
        
        if i < n-m:
            cur_hash = (cur_hash - ord(s[i]) * power) % mod 
            cur_hash = (cur_hash * p + ord(s[i+m])) % mod 
        
    return res 

#Time complexity average O(n+m)  worst O(nm)
#rolling hash O(1) to move the window  

