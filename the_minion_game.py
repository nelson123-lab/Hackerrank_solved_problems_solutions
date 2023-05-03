s = input()
countA =0
countB= 0
vol = "AEIOU"
for i in range(len(s)):
    if s[i] in vol:
        countB = countB + len(s[i:])
    else:
        countA = countA + len(s[i:])
if countA == countB:
    print("draw")
elif countA > countB:
    print("a wins", countA)
else:
    print("b wins", countB)
