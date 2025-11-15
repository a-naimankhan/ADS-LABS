#KMP 

#text = ABABAB  = t 
#pattern = ABABC = p
# 
# A no repeating 
# and ABA one repeating where A is prefix and B is suffix 
# ABAB the same AB prefix and B is the suffix so the as I understand the len of the repeating suffixex is the numbers we are getting so it's 2 
# p = ABABC 
# Cpi = {a:0 , b : 0 , a : 1 , b : 2 , c : 0}
# so actually we move in the pattern we need 
# A B A B A B = t 
# A B A B C = p 
# we don't move to the first A 
# we move to the previoud suffix and add to the beging so there is how we we moved to idx = 2 
# since AB = 2 
# and C != A 
# so we don't look to the very begining but for the next element where A appears and to found it we used the trick above 
# 
# PSEUDOCODE 
# KMP(t , p)
#   lps =  LPS(p) 
#   i , j = 0 , 0 
#   for i < m {
    #if t[i] == p[j]:
        #i++ 
        #j++
        #if j == m-1 
        # res = append(res , i-j) what's the i-j yoo 
        #   
    #else:
        # uf j == 0 :
            #i ++ 
        #else :
        #   j = LPS(j-1) 
#}

#
# LPS(p):
    #lps[0]= 0
    #ln = 0 
    #i = 1 
    #while i < m:
    # if p[i] == p[ln]:
        #ln += 1 
        #lps[i] = ln #we change the prefxi and suffix 
        #i++
    # else case for scenario when it didn't become 0 
    #like for ex AAAA so the suffix becomes 1 , 2 , 3 , 3 not the 1 , 2 , 3 , 0 
    # else:
        #if ln != 0:
            #ln-- #I voobshe ne ponimayu che nahoi proishodit  
        #else: 
            #i++ 
    #}
#  #O(n+m)   
#  


def build_lps(p):
    lps = [0] * len(p)
    length = 0
    i = 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    res = []
    i = j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            res.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res

print(kmp("ABABAB", "ABABC"))
