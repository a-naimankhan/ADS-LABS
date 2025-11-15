def lower_bound(nums , target):
    l , r = 0 , len(r)
    res = -1 
    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            res = m 
            r = m -1 
        elif target > nums[m]:
            l = m+1 
        else:
            r = m 
    return res  


n , m = map(int , input().split())

nums = list(map(int , input().split()))

lb = lower_bound(nums , m)
if lb != -1:
    print(lb + 1)
else:
    print(lb)


