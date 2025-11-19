#Дана строка S и шаблон P.
#Требуется найти количество всех вхождений P в S.

def rabin_karp(s , pat):
    n , m = len(s) , len(pat)
    counter = 0 

    if m > n:
        return 0 
    
    p = 31 
    mod = 10 ** 9 + 9 

    pah_hash = 0 
    for c in pat:
        pat_hash = (pat_hash * p + ord(c)) % mod 
    
    cur_hash = 0 
    for c in s[:m]:
        cur_hash = (cur_hash * p + ord(c)) % mod 
    
    power = pow(p , m-1 , mod) 

    for i in range(n-m+1):
        if cur_hash == pat_hash:
            if s[i:i+m] == pat:
                counter += 1 
        
        if i < n-m:
            cur_hash = (cur_hash - ord(s[i]) * power) % mod #remove left  
            cur_hash = (cur_hash * p + ord(s[i+m])) % mod  #add right  

    return counter 


s = input() 
p = input() 

print(rabin_karp(s , p))

