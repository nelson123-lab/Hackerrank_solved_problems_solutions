
import array

n = int(input())
arr = list(map(int, input().rstrip().split()))
for no in range(n):
    s= arr[n-1]
    n -= 1
    print(s,end = ' ')
