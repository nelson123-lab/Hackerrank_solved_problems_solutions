from itertools import combinations_with_replacement

input1 = input().split(" ")
word, no = "".join(sorted(input1[0])), int(input1[1])
print("\n".join(["".join(i) for i in list(combinations_with_replacement(word, no))]))
