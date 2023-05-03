def capital(word):
    result=""
    for i in range(len(word)):
        if word[i].isalpha():
            result = result + word[i].upper() +word[i+1:]
            break
        elif word[i].isdigit():
            result1 = word[i:]
            break
        else:
            result = result + word[i]
            i =i+1
    return result
s= input()
a=[]
for i in s.split(" "):
    a.append(capital(i))
print(" ".join(a))
