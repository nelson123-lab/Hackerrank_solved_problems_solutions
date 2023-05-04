import numpy as np

a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
z= a*b
a=[]
print(z)
for n in z:
    a.append(n)
print(a)
