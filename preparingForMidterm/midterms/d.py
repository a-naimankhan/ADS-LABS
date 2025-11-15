def upper_bound(nums , target):
    l , r = 0 , len(r)
    while l < r:
        m = (l+r) // 2 
        if target >= nums:
            l = m + 1 
        else:
            r = m 
    return l  

n , k = map(int , input().split())
nums = list(map(int , input().split()))

up = upper_bound(nums , k)
if up == len(nums):
    print(-1)
else:
    print(up)
