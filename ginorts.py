"""
Sorting1234
lower_case | upper_case | odd_digits | even_digits


ginort          S           13             24

"""
S = sorted(input())
upper_case_letter = ""
lower_case_letter = ""
odd_no = ""
even_no = ""
for i in S:
    if i.islower():
        lower_case_letter += i
    elif i.isupper():
        upper_case_letter += i
    elif int(i)% 2 != 0:
        odd_no += i
    else:
        even_no += i

print(lower_case_letter + upper_case_letter + odd_no + even_no)
