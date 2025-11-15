import sys


mod = 10 ** 9 + 7 
base = 11  

#func compute_hash(s):'
    #where I use just formula 
    #hash = (hash + (ord(ch) -47) * power ) % mod 
def compute_hash(s):
    h = 0
    power = 1 
    for ch in s:
        h = (h + (ord(ch) - 47) * power) % mod 
        power = (power * base) % mod
    return h  

n = int(input())
data = sys.stdin.read().strip().split()
n = int(data[0])
arr = data[1:]


#pseudocode 
#for x in data 
    #if it is hash: 
        #add to hashes 
    #else it is a string 
        #add to strings 
#for x in data:
#    if x.isdigit():
#        val = int(x)
#        hashes.add(val) 
##    else:
 #       strings.append(x)


vals = [int(x) for x in arr]

for s in arr:
    h = compute_hash(s)
    if h in vals:
        print(f'Hash of string "{s}" is {h}') 
#calculate for hash of strings:
    #call computting hash 
    #check if it is already in the vals 
    #print it
#for s in strings:
  #  h = compute_hash(s)
  #  if h in hash:
        #print(f'Hash of string "{s}" is {h}') 