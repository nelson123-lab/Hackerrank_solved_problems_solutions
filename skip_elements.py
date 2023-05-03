l=["a","b","c","d","e"]
p=[]
index =0
for letter in l:
    if index < len(l):
        if letter not in p:
            p.append(l[index])
            index = index + 2
print(p)
