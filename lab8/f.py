s = input().strip()
n = len(s)

p = 131
mod = 10**9 + 9

pref = [0] * (n + 1)
power = [1] * (n + 1)
for i in range(1, n + 1):
    pref[i] = (pref[i-1] * p + (ord(s[i-1]) - 96)) % mod
    power[i] = (power[i-1] * p) % mod

subs = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        cur = (pref[j] - pref[i] * power[j - i]) % mod
        subs.add(cur)

print(len(subs))
