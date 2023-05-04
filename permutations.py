from itertools import permutations

input1 = input().split(" ")
word,no = input1[0],int(input1[1])
result =[]
for i in list(permutations(word, no)):
    result.append("".join(i))
result.sort()
print("\n".join(result))
