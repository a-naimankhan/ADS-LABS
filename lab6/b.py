#IDEA 
#find common numbers in two arrays 
#good solution is to sort everything and then compare 
#then go while both pointers are in range 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + mid + quick_sort(right)
     

n , m = map(int , input().split()) 
nums1 = []
if n > 0:
    nums1 = list(map(int , input().split())) 
    nums1 = quick_sort(nums1)

nums2 = [] 
if m > 0:
    nums2 = list(map(int , input().split())) 
    nums2 = quick_sort(nums2)  



                                    
i = j = 0 
res = []
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        res.append(nums1[i])
        i += 1 
        j += 1 
    elif nums1[i] < nums2[j]:
        i += 1 
    else:
        j += 1  


print(*res)

#time complexity O(n log n + m log m) 
#space complexity O(n + m) 

#I will read two arrays 
#then quick sort both of them
#then use two pointers to find common elements
