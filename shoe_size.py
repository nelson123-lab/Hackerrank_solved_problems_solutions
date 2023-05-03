x = int(input())
shoe_size = list(map(int, input().split()))
shoe_dict = {k: shoe_size.count(k) for k in shoe_size}
cus_no = int(input())
purchases = []
for i in range(cus_no):
    purchases.append([int(i) for i in input().split()])
total = 0
for n in purchases:
    if n[0] in shoe_dict.keys() and shoe_dict[n[0]] >=1:
        total += n[1]
        shoe_dict[n[0]] -= 1
print(total)

"""
sample input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
"""
