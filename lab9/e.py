def prefix_fucntion(s):
    n = len(s)
    pi = [0] * n 
    for i in range(1 , n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j 
    return pi 

t = int(input())
for _ in range(t):
    str = input().split()
    subStr = str[0]
    k = int(str[1])
    pi = prefix_fucntion(subStr)
    n = len(subStr)
    p = pi[-1]
    ans = n + (k-1) * (n-p)
    print(ans)



