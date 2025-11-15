def cyclic_shift(s1 , s2):
    if len(s1) != len(s2):
        return -1 
    doubled = s1+s1 
    pos = doubled.find(s2)
    if pos == -1:
        return -1 
    #return pos
    # calculate shift 
    shift = (len(s1) - pos) % len(s1)
    return shift 


s1 = input().strip() 
s2 = input().strip()
print(cyclic_shift(s1 , s2))
#pseudocode 
#just to check is s2.Find(s1+s1)