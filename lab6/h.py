#pseudocode 
#is to just move pointers and check if the curr > targetted and the least 
#or just sort it and print the next element after target 
#and also to find the next elements I would like to use binary search :d 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def search(arr , target):
    if len(arr) < 2:
        return arr 
    result = arr[0]
    l , r = 0 , len(arr) -1
    while l <= r:
        m = (l + r) // 2 
        if arr[m] > target:
            result = arr[m]
            r = m - 1
        else:
            l = m + 1  
    return result

n = int(input())
letters = input().split()
target = input().strip()

letters = quick_sort(letters)

print(search(letters , target))

#provide binary search to find position? 
