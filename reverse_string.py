a = 'Nelson'
def reverse1(strg):
    lst =[]
    p = -1
    for i in range(len(a)):
        lst.append(a[p])
        p -= 1
        if p < -len(a):
            break
    return "".join(lst)
print(reverse1(a))