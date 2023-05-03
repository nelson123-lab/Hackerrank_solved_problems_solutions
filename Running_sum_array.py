ab = [1, 2, 3, 4]
# b = [a[0]]
a = 0
b = []
for count, ele in enumerate(ab):
    a = a + ele
    b.insert(count,a)
print(b)