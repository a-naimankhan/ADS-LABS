import sys 
input = sys.stdin.readline 

n = int(input())
ducks = list(map(int , input().split()))

mn = min(ducks)
s = sum(ducks)

ans = s + mn * (n-2)

print(ans)