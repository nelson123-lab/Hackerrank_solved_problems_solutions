arr = list(map(int, input().split()))
s = Noner
l = None
index1 = 0
index2 = 0
for count, value in enumerate(arr):
    if s is None or s > value:
        s = value
        index1 = count
    if l is None or l < value:
        l = value
        index2 = count
    else:
        pass
print(sum(arr[:index1]+ arr[index1+1:]))
print(sum(arr[:index2]+ arr[index2+1:]))