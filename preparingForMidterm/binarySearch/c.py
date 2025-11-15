def lower_bound(arr , x):
    l , r = 0 , len(arr)
    while l < r:
        m = (l+r) // 2
        if x > arr[m]:
            l = m+1 
        else:
            r = m 
    return l 

def upper_bound(arr , x):
    l , r = 0 , len(arr)
    while l < r:
        m = (l+r) // 2 
        if x >= arr[m]:
            l = m+1 
        else:
            r = m  
    return l 

n = int(input()) 
arr = list(map(int , input().split()))
x = int(input())

lb = lower_bound(arr , x)
ub = upper_bound(arr , x)

if lb == len(arr) or arr[lb] != x:
    print("-1 -1")
else:
    print(lb , ub-1)  