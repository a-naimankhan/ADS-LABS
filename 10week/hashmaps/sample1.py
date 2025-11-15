#pseudocode 
#t = ABABCABA 
#look for specific pattern
#needPatter = ABABD 
#the first idea to get two pointer i j 
#and move both of them while their the saem 
#if s[i] == needPattern[j] and j <= needPattern:
    #i++ 
    #j++ 
#elif not equal:
    #j == 0 
# 

#O(nm) where n = the whole string and m is needed pattern 



#Second keys 
#t = CBABCABA 
#needeePattern = ABC
#sumOfPattern = [x for x in neededPattern sum += normalize(x)]
#


#def normalize(char) {
    #return char - 65
#}


#hz che tam proishodit 
#v konce koncov sdelali nekyi sliding window chto by naity sybsequense 

#case with polynomial  
#CBABCABA  
#case = b^m-1x1 + bm-2 x2 ... 
#where m = is the number 

#pattern = ABS 
#hash of the pattern : 10^2 1 + 10^1 + 2 + 10^0 + 3 = 123 
#doing some calc in the pattern  
#after doing it compare it with the pattern 
#and since it's not equal move l pointer and r pointer 
#as in the sliding window 
#and once we found 
#but it's not like i thought since I also have to check the power of 10 
#so there is a formula where fn = (h(n-1) - 10**n -1) * 10 - hn) 


#some real pseudocode 
#RK = (t , p)
#b = 31 
#pH = p[0] -'A' + 1
#textHast = t[0] - 'A' + 1  
#md = 10 * 9 + 7 #I don't even understand why we need this largest prime number :d 
#
#for i = 1 ; i <= m ; i++ {
    #pH = pH * b + (p[i] - A + 1) % md  
    #tH = tH * b + (t[i] - 'A' + 1) % md 
#}

#for i = 0 ; i < n - m;  i++ {
    #if ph == th:
        #res.append(ph)     
    #if i < n-m
        #th = th - t[i]) * 10 ** n-1) * b + t*(t[i] + m -'A' + 1)
#}



def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    b = 31
    mod = 10**9 + 7
    
    # helper to map A->1, B->2, ...
    def val(c):
        return ord(c) - ord('A') + 1
    
    # compute initial hashes
    p_hash = 0
    t_hash = 0
    power = 1  # b^(m-1)
    
    for i in range(m):
        p_hash = (p_hash * b + val(pattern[i])) % mod
        t_hash = (t_hash * b + val(text[i])) % mod
        if i < m - 1:
            power = (power * b) % mod
    
    res = []
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                res.append(i)
        if i < n - m:
            t_hash = ((t_hash - val(text[i]) * power) * b + val(text[i + m])) % mod
            if t_hash < 0:
                t_hash += mod
    
    return res

