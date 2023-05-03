from operator import itemgetter
nm = list(map(int, input().split()))
n,m = nm[0], nm[1]
rows=[]
for i in range(n):
    rows+= [list(map(int, input().split()))]
k = int(input())
arr = sorted(rows, key=itemgetter(k))
for i in arr:
    print(*i)
