import re
link = open('C:/Users/NELSON JOSEPH/Desktop/info.txt','r')
a = []
for i in link.readlines():
    if i == "\n":
        pass
    else:
        p = i.rstrip()
        a.append(p)
Result = {p: a.count(p) for p in a}
Sorted = dict(sorted(Result.items(), key=lambda item: item[1]))
print(Sorted)
{'Abhijeet': 5, 'Devesh': 14, 'Nelson': 16, 'Jyotirnav': 17, 'Amit Bisht': 19, 'Aswathy': 23, 'Nikhil': 26, 'Abdullah': 27}
{'Abhijeet': 5, 'Devesh': 14, 'Nelson': 16, 'Jyotirnav': 17, 'AmitBisht': 19, 'Aswathy': 23, 'Nikhil': 26, 'Abdullah': 27}