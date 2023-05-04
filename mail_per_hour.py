name = input("Enter file:")
if len(name) < 1 : name = "mail.txt"
handle = open(name)
fr = handle.readlines()
time_bk =dict()
l=[]
t=[]
for lines in fr:
    if lines.startswith("From "):
        time = lines.split()[5]
        l.append(time.split(':')[0])
for num in l:
    time_bk[num] = time_bk.get(num,0) + 1
for k,v in time_bk.items():
    t.append((k,v))
t.sort()
for element in t:
    print(str(element[0]) + " " + str(element[1]))
