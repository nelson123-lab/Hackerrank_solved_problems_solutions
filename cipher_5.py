def cipher_5(message):
    """
    Each alphabet is shifted to the 5th alphabet
    """
    alpha = []
    a = "A"
    for i in range(1,27):
        alpha.append(a)
        a = chr(ord(a)+1)
    output =''
    for i in message:
        if i.isupper():
            output += alpha[(alpha.index(i)+5)%26]
        elif i.islower():
            output += alpha[(alpha.index(i.upper())+5)%26].lower()
        else:
            output += i
    return output

a = input("Enter the code to be encoded")
print(cipher_5(a))

"""
INPUT = "jjajfzzsjfjd"
OUTPUT = "oofokeexokoi"
"""