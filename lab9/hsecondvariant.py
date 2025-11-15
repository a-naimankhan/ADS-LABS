def z_function(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def count_splits(s):
    n = len(s)
    z = z_function(s)
    count = 0
    for i in range(1, n // 2 + 1):
        if z[i] >= i and n > 2 * i:
            count += 1
    return count

# Пример:
s = input().strip()
print(count_splits(s))
