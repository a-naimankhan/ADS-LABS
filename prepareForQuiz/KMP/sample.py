def build_lps(p):
    lps = [0] * len(p)
    j = 0 

    for i in range(1 , len(p)):
        while j > 0 and p[i] != p[j]:
            j = lps[j-1]
        if p[i] == p[j]:
            j += 1 
        lps[i] = j 
    return lps  


def kmp_search(s ,p):
    lps = build_lps(p)
    res = [] 
    j = 0 

    for i in range(len(s)): 
        while j > 0 and s[i] != s[j]:
            j = lps[j-1]
        if s[i] == p[j]:
            j += 1 
        if j == len(p):
            res.append(i-j+1)
            j = lps[j-1]
    return res  

#build lps O(m) 
#Search lps O(n)

