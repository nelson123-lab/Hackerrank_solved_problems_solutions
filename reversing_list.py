list = [2,4,6,1,4,5,6,3,1]
p = len(list)
print(p)
index = p
for no in list:
    s= list[p-1]
    p -= 1
    print(s,end = ' ')
