n = int(input())
a = []
sum_right = 0
sum_left = 0
for i in range(n):
    e = list(map(int, input().split()))
    # a.append(e)
    sum_right += e[i]
    sum_left += e[n-1-i]
print(a)
print(sum_right)
print(sum_left)
