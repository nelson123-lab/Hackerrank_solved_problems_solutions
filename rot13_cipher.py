def rot13(message):
    alpha = []
    a = "A"
    for i in range(1,27):
        alpha.append(a)
        a = chr(ord(a)+1)
    output =''
    for i in message:
        if i.isupper():
            output += alpha[(alpha.index(i)+13)%26]
        elif i.islower():
            output += alpha[(alpha.index(i.upper())+13)%26].lower()
        else:
            output += i
    return output

"""
alphabet = []
p = 'a'
for i in range(1,27):
    alphabet.append(p)
    p = chr(ord(p)+1)

def rot13(message):
    cipher_text = ''
    for i in message:
        if i.isupper():
            p = i.lower()
            a = (alphabet.index(p) + 13)%26
            cipher_text = cipher_text + alphabet[a].upper()
        else:
            a = (alphabet.index(i) +13)%26
            cipher_text = cipher_text + alphabet[a]

    return cipher_text
"""