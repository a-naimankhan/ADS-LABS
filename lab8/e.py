n = int(input())
p = list(map(int, input().split()))

#pseudocode
#is to re collect the hash into the char 

res = []
prev = 0
for i in range(n):
    char_val = 97 + (p[i] - prev) // (2 ** i)
    res.append(chr(char_val))
    prev = p[i]

print("".join(res))
