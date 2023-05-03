def solution(s):
    lst = []
    x=0
    while x  < len(s)-1:
        lst.append(s[x:x+2])
        x += 2
    if x == len(s)-1:
        lst.append(s[x]+"_")
    return lst
print(solution("asdfadsf"))
print(solution("sdhfjds"))