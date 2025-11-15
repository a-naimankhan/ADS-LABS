n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

res = []

i, j = 0, 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] > nums2[j]:
        res.append(nums2[j])
        j += 1
    else:
        res.append(nums1[i])
        i += 1

while i < len(nums1):
    res.append(nums1[i])
    i += 1

while j < len(nums2):
    res.append(nums2[j])
    j += 1

for num in res:
    print(num, end=" ")
