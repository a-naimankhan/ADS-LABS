def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x[0] < pivot[0] or (x[0] == pivot[0] and (x[1] < pivot[1] or (x[1] == pivot[1] and x[2] < pivot[2])))]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x[0] > pivot[0] or (x[0] == pivot[0] and (x[1] > pivot[1] or (x[1] == pivot[1] and x[2] > pivot[2])))]
    return quick_sort(left) + mid + quick_sort(right)


n = int(input())
dates = []

for _ in range(n):
    d, m, y = input().split('-')
    dates.append((int(y), int(m), int(d), f"{d}-{m}-{y}"))

dates = quick_sort(dates)

for _, _, _, original in dates:
    print(original)
