with open("C:/Users/NELSON JOSEPH/Desktop/text.txt","r") as fileread:
    with open("C:/Users/NELSON JOSEPH/Desktop/text1.txt","w") as filewrite:
        for line in fileread:
            filewrite.write(line.upper())
