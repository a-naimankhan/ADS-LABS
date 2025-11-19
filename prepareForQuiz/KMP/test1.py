#Дана строка S и шаблон P.
#Требуется найти количество всех вхождений P в S.
def build_lps(p):
    lps = [0] * len(p)
    j = 0 

    for i in range(1 , len(p)):
        while j > 0 and p[i] != p[j]:
            j = lps[j-1]
        if p[i] == p[j]:
            j += 1 
        return lps 


def lps(s , p):
    lps = build_lps(p)
    counter = 0 
    j = 0 

    for i in range(len(s)):
        while j > 0 and s[i] != s[j]:
            j = lps[j-1]
        if s[i] == p[j]:
            j += 1  
        if j == len(p):
            counter += 1 
            j = lps[j-1]
    return counter 

#tut navernoe nu takoe sebe честно говоря я просто списал с сэмпла который писал раньше 
#no budto by kazhetsya chto ya mogu dazhe prosto zaprintin poslednyi prefix which != 0 
#no tozhe maloveroyanto dazhe 


def build_lps(p):
    lps = [0] * len(p)
    j = 0

    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = lps[j-1]

        if p[i] == p[j]:
            j += 1
            lps[i] = j

    return lps


def kmp_count(s, p):
    lps = build_lps(p)
    count = 0
    j = 0

    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = lps[j-1]

        if s[i] == p[j]:
            j += 1

        if j == len(p):
            count += 1
            j = lps[j-1]   # continue matching

    return count


s = input().strip()
p = input().strip()
print(kmp_count(s, p))


s = input() 
p = input() 

print(lps(s , p))