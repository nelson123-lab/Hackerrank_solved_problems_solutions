import sys

a=[]
for line in sys.stdin:
    a.append(line.rstrip())
e = a[0]
eng_roll = a[1].strip().split()
f = a[2]
fre_roll = a[3].strip().split()
eng= set(eng_roll)
print(len(eng.intersection(set(fre_roll))))
