lst = [1, 2, 3, 3, 3, 3, 2, 2, 1, 1, 1, 4, 4, 5, 3] 
preced = set()
res = {}
for idx, val in enumerate(lst, start = 1):
    if val not in preced:
        preced.add(val)
        res[val] = [idx]
    else:
        res[val] += [idx]
print(res)
 

