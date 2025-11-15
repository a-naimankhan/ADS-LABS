n = int(input())
str = input()
vowels = "aeiou" 


def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + mid + quick_sort(right)
     

v = [ch for ch in str if ch in vowels] 
c = [ch for ch in str if ch not in vowels]

v = quick_sort(v)
c = quick_sort(c)
print("".join(v + c))
#pseudocode 
#res = ""
#if vowel in vowels:
#    res += vowel 
#for ch in str: 
#if ch is not in vowels: 
    #res += ch 

#print(res)

#time complexity O(n) 
#space complexity O(n) 
#I have to sort the vowels first and then the consonants 
#then concatenate them 
#finally print the result 
#vowels = "" 
#consonants = "" 
#once I have both I can I should quick sort them 
#def quick_sort(arr , l , r):
    #if pivot is not 'a' or 'o' or 'b' or 'lastconsonant' 
    # then do the quick sort 
    #  

