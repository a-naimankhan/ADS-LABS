def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quick_sort(left) + mid + quick_sort(right)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for col in range(m):
    column_values = [matrix[row][col] for row in range(n)]
    
    column_values = quick_sort(column_values)
    
    for row in range(n):
        matrix[row][col] = column_values[row]

for row in range (n):
    for col in range(m):
        print(matrix[row][col] , end = " ")
    print()
