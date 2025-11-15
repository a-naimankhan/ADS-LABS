def overlap_suffix_prefix(p, city):
    p = p.lower()
    city = city.lower()
    max_len = min(len(p), len(city))
    for i in range(max_len, 0, -1):
        if p[-i:] == city[:i]:
            return i
    return 0

P = input().strip()
n = int(input())
cities = [input().strip() for _ in range(n)]

best_len = 0
best_cities = []

for city in cities:
    overlap = overlap_suffix_prefix(P, city)
    if overlap > best_len:
        best_len = overlap
        best_cities = [city]
    elif overlap == best_len and overlap != 0:
        best_cities.append(city)

if best_len == 0:
    print(0)
else:
    print(len(best_cities))
    for c in best_cities:
        print(c)
