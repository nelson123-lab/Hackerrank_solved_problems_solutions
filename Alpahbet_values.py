def max_value(str1, str2):
    sum1=0
    sum2=0
    for i in str1:
        sum1 = sum1 + (alpha_list.index(i) +1)
    for i in str2:
        sum2 = sum2 + (alpha_list.index(i) +1)
    return max(sum1, sum2)

str1 = input().split()[1]
str2 = input().split()[1]
alpha = 'a'
alpha_list = []
for i in range(1, 27):
    alpha_list.append(alpha)
    alpha = chr(ord(alpha) +1)
print(max_value(str1, str2))
