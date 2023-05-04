# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = list(map(int, input().split()))

#To find the mean
m = sum(x) / len(x)
print("{:.1f}".format(m))

# To find the meadian
x = sorted(x)
if n % 2 == 1:
    m = x[n // 2]
    print(m)
else:
    m = (x[n // 2 - 1] + x[n // 2]) / 2
    print("{:.1f}".format(m))

#To find the mode
d = {}
count = 1
for i in x:
    if i not in d:
        count = 1
        d[i] = count
    else:
        count +=1
        d[i] = count

# converts the data with intensities as values as the data is already sorted earlier

if sum(d.values()) == n: #To check if intensities of all values are 1
    print(x[0])             #lowest value as x[0] will be the lowest (sorted)
else:
    print(d[max(d.values())])  #Key with the maximum intensity
