from itertools import combinations

input1 = input().split(" ")
word, no = "".join(sorted(input1[0])), int(input1[1])
for n in range(1,no+1):
    print("\n".join(["".join(i) for i in list(combinations(word,n))]))
