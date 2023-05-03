fname = input("Enter file name: ")
fh = open(fname)
fr = fh.read()
l = list()
fs = fr.split()
for element in fs:
    if element not in l:
        l.append(element)
l.sort()
print(l)
