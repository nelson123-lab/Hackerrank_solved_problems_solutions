def remove_duplicate(string):
    new = ""
    for i in string:
        if i not in new and string.count(i) >= 1:
            new += i
    return new
s = input()
no = int(input())
new_list = []
for i in range(len(s)):
    if i % no == 0 and i < len(s):
        new_list.append(remove_duplicate(s[i:i+no]))
print("\n".join(new_list))
