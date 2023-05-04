'''Method 1'''
def is_isogram(string):
    #your code here
    if len(string) == 0:
        return True
    string1 = string.lower()
    if sorted(set(string1)) == sorted(list(string1)):
        return True
    else:
        return False

"""Method 2"""
string = input()
def duplicate(string):
    lst = []
    for i in string:
        if i in lst:
            return False
            break
        else:
            lst.append(i)
    return True
print(duplicate(string))

"""Method 3"""
def is_isogram(string):
    return len(string) == len(set(string.lower()))
print(is_isogram(input()))
#fails when there is large no of letters.
