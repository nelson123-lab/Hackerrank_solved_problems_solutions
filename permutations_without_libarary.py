def perm1(lst):# n! space complexity
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l =[]
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l

data = list("abc")
print("perm1")
for p in perm1(data):
    print(p)

def perm2(lst):# constant space complexity
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        l =[]
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                yield [x]+p

print("perm2")
for p in perm2(data):
    print(p)
