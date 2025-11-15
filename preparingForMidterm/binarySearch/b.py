def lower_bound(nums , target):
    l , r = 0 , len(nums) - 1
    while l < r:
        m = (l+r) // 2 
        if target > nums[m]:
            l = m+1 
        else:
            r = m  

    return l 

def upper_bound(nums , target):
    l , r = 0 , len(nums)
    while l < r:
        m = (l+r) // 2
        if target >= nums[m]:
            l = m+1 
        else:
            r = m 
    return l 
n = int(input())
arr = list(map(int , input().split())) 
x = int(input())

print(lower_bound(arr , x))