n = int(input())
l={}
count = 0
for _ in range(n):
    p = input()
    if p not in l:
        l[p] = 1
        count += 1
    else:
        l[p] +=1
print(count)
print(*l.values())
