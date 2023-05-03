import re

path = "C:\\Users\\NELSON JOSEPH\\Desktop\\bill.txt"
bill = open(path)
a = []
for i in bill.readlines():
    a.append(int("".join(re.findall("\d", i))))
print(sum(a))