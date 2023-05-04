
nm = list(map(int, input().split(" ")))
n, m = nm[0], nm[1]
arr1 = list(map(int, input().split(" ")))
lst=[]
for _ in range(2):
  lst.append(set(map(int, input().split(" "))))
A, B =lst[0], lst[1]
def happiness(array, A, B):
    happiness = 0
    for i in array:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1
    return happiness
print(happiness(arr1, A, B))
