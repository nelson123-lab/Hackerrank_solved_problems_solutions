n = int(input())
a = []

slot_count = 0
for i in range(n):
    a.append(input())
removal_count = len(a[0])

def largest_removal(string):
    return "".join(sorted(string))[:-1]

def largest_all(lst):
    return sorted("".join(lst))[-1]


total_spins = 0

['123','232','232','734']

for i in range(removal_count):
    total_spins += int(largest_all(a))
    for idx, ele in enumerate(a):
        a[idx] = largest_removal(ele)
print(total_spins)