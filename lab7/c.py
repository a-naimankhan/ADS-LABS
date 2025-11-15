n , m = map(int , input().split())
nums1 = []
if n > 0:
    nums1 = list(map(int , input().split()))

nums2 = []
if m > 0:
    nums2 = list(map (int , input().split()))

nums1.sort()
nums2.sort()

i , j = 0 , 0 
res = []
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        res.append(nums1)
        i += 1 
        j += 1 
    #elif nums1[i] != nums2[j] and array still had to had the elements 
    #i mean I should sort( 
    elif nums1[i] < nums2[j]:
        i += 1 
    elif nums2[j] < nums1[i]:
        j += 1  
    
while i < len(nums1):
    res.append(nums1)
    i += 1 

while j < len(nums2):
    res.append(nums2)
    j += 1 

for num in res:
    print(num , end=" ")