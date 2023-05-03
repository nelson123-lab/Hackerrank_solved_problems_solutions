def string(text):
    str = ''
    new = []
    for i in text:
        if i !='.' and i != '!' and i != '?':
            str = str +i
        else:
            new.append(str +i + " ")
            str = ''
    return new
text = "Hi! This is the article you have to format properly. Could you do that for me, please?"
print(string(text))