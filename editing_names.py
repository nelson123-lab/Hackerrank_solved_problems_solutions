def pig_latin(text):
    list=[]
    string=""
    # Separate the text into words
    for word in text.split():
        list.append(word[1:]+word[0]+"ay")
    # Create the pig latin word and add it to the list
    # Turn the list back into a phrase
    return " ".join(list)

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
