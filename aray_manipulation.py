n, m = map(int, input().split())
lst =[0]*(n+1)
for _ in range(m):
    a, b, k = map(int, input().split())
    lst[a-1] +=k
    if b<= len(lst):
        lst[b]-=k
maxx = 0
sum1 = 0
for i in lst:
    sum1 += i
    if sum1>maxx:
        maxx = sum1
print(maxx)
