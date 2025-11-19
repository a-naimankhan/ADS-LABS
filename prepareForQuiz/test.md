1) Merge Sort complexity
What is the time complexity of merge sort in the worst case?
a) O(n²)
b) O(n log n)
c) O(log n)
d) O(n)

2) Merge operation
How much time does the merge step take for two sorted subarrays of total length n?
a) O(log n)
b) O(n)
c) O(n²)
d) O(1)

3) Rabin–Karp hashing
Given base = 31, mod = 1e9+9, compute the hash of the string "AB":
Use formula:
h = (h * 31 + ord(char)) % mod
(ord('A') = 65, ord('B') = 66)
a) 65
b) 2081
c) 2015
d) 66

4) Rabin–Karp window shift
Which formula correctly removes the left character during sliding?
Let left char = s[i], pattern length = m, base = p.
a) h = h - ord(s[i]) * p^(m-1)
b) h = h - ord(s[i]) * p
c) h = h // p
d) h = ord(s[i+1])

5) KMP – LPS meaning
What does lps[i] represent?
a) Number of mismatches before i
b) Longest prefix which is also a suffix ending at i
c) Index of previous mismatch
d) Amount of characters skipped

6) KMP – complexity
What is the worst-case time complexity of KMP?
a) O(n²)
b) O(n+m)
c) O(n log n)
d) O(log n)

7) BFS queue behavior
Which data structure does BFS use?
a) Stack
b) Queue
c) Priority queue
d) Dictionary

8) BFS on adjacency matrix complexity
Let graph have V nodes.
What is the time complexity of BFS on adjacency matrix?
a) O(V)
b) O(V²)
c) O(E)
d) O(V + E)

9) Adjacency list memory
What is the memory usage of adjacency list?
a) O(V²)
b) O(V + E)
c) O(E²)
d) O(V log V)

10) Hash table worst-case
What is the worst-case time complexity for search in a hash table?
a) O(1)
b) O(log n)
c) O(n)
d) O(n log n)

ans: 
    1) b 
    2) b 
    3) b  
    4) a  
    5) b 
    6) I guess it is O(n + m) tbh I can't even understand why 
    7) b 
    8) b saving O(v^2) getting O(1) inserting could also be O(v^2) in worst case  
    9)