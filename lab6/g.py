n = int(input())

old_to_new = {} 
new_to_old = {} 

for _ in range(n):
    old , new = input().split() 

    if old in new_to_old:
        original = new_to_old[old] 
        old_to_new[original] = new 
        new_to_old[new] = original 
        del new_to_old[old] 
    else:
        old_to_new[old] = new 
        new_to_old[new] = old 

sorted_items = sorted(old_to_new.items(), key=lambda x: x[0])

print(len(sorted_items))
for old, new in sorted_items:
    print(old, new)