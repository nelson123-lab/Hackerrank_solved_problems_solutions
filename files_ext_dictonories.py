name = input("Enter file:")
handle = open(name)
fr = handle.readlines()
p =dict()
l=[]
for lines in fr:
    if lines.startswith("From:"):
        l.append(lines.split()[1])
for word in l:
    p[word] = p.get(word,0) + 1
#max fuction for finding maximum value
"""
x =max(p.values())
for key,value in p.items():
    if x== value:
        print(key+" "+str(value))
"""
#method 2 using largest smallest
largst_value = None
largst_key   = None
for key,value in p.items():
    if largst_value is None or value > largst_value:
        largst_value = value
        largst_key = key
print(largst_key+" "+str(largst_value))

"""
to sort dictonaries according to the values
p = sorted(record.items(),key=lambda x: x[1])
print(p)
"""
