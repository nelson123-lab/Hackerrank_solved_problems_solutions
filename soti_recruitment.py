def palindrome(num):
    p =str(num)
    if p == p[::-1]:
        return num
    return palindrome(num+1)

def covert(list):
    s = [str(i) for i in list]
    print(s)
    res =int("".join(s))
    return res
list = [1,2,3]
print(palindrome(covert(list)))
