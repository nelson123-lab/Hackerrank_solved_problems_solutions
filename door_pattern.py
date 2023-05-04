nm =list(map(int, input().split()))
n,m =nm[0],nm[1]
a="WELCOME"
b=".|."
for i in range(1,n):
    if i%2!=0:
        print((b*i).center(m,"-"))
print(a.center(m,"-"))
for i in range(n-1,0,-1):
    if i%2!=0:
        print((b*i).center(m,"-"))
