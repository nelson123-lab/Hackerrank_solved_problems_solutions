def reverse(n):
    m = 0
    while n > 0:
        n, r = divmod(n, 10)
        m = 10 * m + r
    return m

print(reverse(123240))
a = -1124
print(int("-"+str(a)[1:][::-1]))
print(divmod(25, 10))
print(divmod(2, 10))
x = 123
s = str(x) 
print(s[1:])