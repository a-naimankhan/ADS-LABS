def search(nums , target):
    l , r = 0 , len(nums) - 1 
    while l <= r:
        m = (l+r) // 2
        if nums[m] == target:
            return m 
        elif target < nums[m]:
            r = m-1  
        elif target > nums[m]:
            l = m+1 
    
    return -1 

n = int(input())
nums = list(map(int , input().split()))
target = int(input())
print(search(nums , target))