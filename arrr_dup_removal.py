def rem_dup(arr):
    for i in arr:
        if arr.count(i) >1:
            arr.remove(i)
            rem_dup(arr)
    return sorted(arr)

def rem1_dup(arr):
    return list(set(arr))

def rem2_dup(arr):
    res =[]
    [res.append(x) for x in arr  if x not in res]
    return res

print(rem_dup([1,2,3,4,4,4,2,1]))
print(rem1_dup([1,2,3,4,4,4,2,1]))
print(rem2_dup([1,2,3,4,4,4,2,1]))
print(rem3_dup([1,2,3,4,4,4,2,1]))
