import sys 
input = sys.stdin.readline 

n , q = map(int , input().split())

compat = [list(map(int  , input().split())) for _ in range(n)]

for _ in range(q):
    arr = list(map(int , input().split()))
    arr = [x - 1 for x in arr] 

    ok = True  

    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if compat[arr[i][arr[j]]] == 0:
                ok = False 
                break 
            if not ok:
                break 
print("YES" if ok else "NO")