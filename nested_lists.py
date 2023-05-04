"""
Given the names and grades for each student in a class of  students,
store them in a nested list and print the name(s) of any student(s) having the
second lowest grade.
Note: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

"""
import sys
a=[]
for line in sys.stdin:
    a.append(line.rstrip())
students_no = a[0]
record ={}
a.remove(a[0])


for n in range(len(a)):
    if n % 2==0 :
        record[a[n]] = float(a[n+1])
rev_record ={}
for key,value in record.items():
        if value in rev_record:
            rev_record[value].append(key)
        else:
            rev_record[value] = [key]
f=sorted(rev_record.items())
n =f[1][1]
if len(n)>1:
    n.sort()
    print("{}\n{}".format(n[0],n[1]))
else:
    print(n[0])
