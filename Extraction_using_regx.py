"""
import re

file = input("Enter the file name")
sum1 =[]
a=[]
fh = open(file)
fr = fh.readlines()
for lines in fr:
    if not re.findall('[0-9]+',lines)==[]:
        sum1.append(re.findall('[0-9]+',lines))
for n in sum1:
    if len(n)==1:
        a.append(int(n[0]))
    elif len(n)==2:
        a.append(int(n[0])+int(n[1]))
    else:
        a.append(int(n[0])+int(n[1])+int(n[2]))
print(sum(a))
"""
import re

f = open("actual_data.txt", 'r')
total = sum([int(i) for i in re.findall('\d+', f.read())])

print(total)
