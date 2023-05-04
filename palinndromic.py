def is_palindrome(input_string):
    input_string1 =input_string.replace(" ","").lower()
    if input_string1 ==input_string1[::-1]:
        return "{} is palindromic".format(input_string)
    else:
        return "{} is not palindromic".format(input_string,)

print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abc"))
print(is_palindrome("kayak"))
