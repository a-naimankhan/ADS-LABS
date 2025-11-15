n = int(input())
nums = list(map(int , input().split()))

#pseudocode      
#find  least absolute difference if there are two elements print all possible pairs 

#Поидее есть два варианта 
# первый пройтись по массиву и найти мин разницу по отдельности и типо уанс я нахожу я возвращаю дикшинари элементов где кей это разница а значение это список кортежей
# второй вариант это отсортировать массив и потом идти по нему и искать минимальную разницу между соседними элементами 
# ну в первом случае O(n^2) во втором O(n log n) + O(n) = O(n log n) 
def quick_sort(nums):
    if len(nums) <= 1:
        return nums 
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

nums = quick_sort(nums) 
min_diff = float('inf') 
res = [] 
for i in range(1 , n):
    diff = nums[i] - nums[i - 1] 
    if diff < min_diff:
        min_diff = diff  
        res = [(nums[i - 1] , nums[i])]
    elif diff == min_diff:
        res.append((nums[i - 1] , nums[i]))
        
for pair in res:
    print(pair[0] , pair[1] , end= " ")