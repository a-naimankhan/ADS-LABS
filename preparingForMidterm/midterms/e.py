def search(n):
    l , r = 2 , n 
    while l < r:
        m = (l + r) // 2
        if m*m == n:
            return True
        elif m*m < n:
            r = m-1 
        else:
            l = m+1
    return False  

n = int(input())

if search(n):
    print("YES")
else:
    print("NO")
