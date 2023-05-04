# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

nm = list(map(int, input().split()))
n,m = nm[0],nm[1]
d = defaultdict(list)
for i in range(1,n+1):
    d[input()].append(i)
l=[]
for n in range(m):
    l.append(input())
for k in l:
    if k in d.keys():
        print(*d[k])
    else:
        print(-1)
    
