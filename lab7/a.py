def merge_sort(words):
    if len(words) <= 1:
        return words 
    
    mid = len(words) // 2 
    left = merge_sort(words[:mid])
    right = merge_sort(words[mid:])

    return merge(left , right)

def merge(left ,right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            res.append(left[i])
            i += 1
        elif len(right[j]) < len(left[i]):
            res.append(right[j])
            j += 1  
        
        else:
            res.append(left[i])
            i += 1 

    res.extend(left[i:])
    res.extend(right[j:])
    return res 

T = int(input())

for _ in range (T):
    words = input().split() 
    sorted_words = merge_sort(words)
    print(*sorted_words)