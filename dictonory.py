dictonary = dict()
words = ['hello','hi','hi','hello','poda','patti','hello']
for word in words:
    dictonary[word] = dictonary.get(word,0)+1
for key,values in dictonary.items():
    print("{} = {}".format(key,values))
