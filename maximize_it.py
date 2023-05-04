from itertools import product

km = list(map(int, input().split()))
k,m = km[0], km[1]
k_lists = []
for i in range(k):
    k_lists.append(list(map(int, input().split()[1:])))
p = map(lambda x:sum(i*i for i in x)%m,product(*k_lists))
print(max(p))
