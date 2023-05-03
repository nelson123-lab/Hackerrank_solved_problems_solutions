n = int(input())
test = []
fin_out = []
for i in range(n):
    test.append(int(input()))
def Triprime_checker(test):
    lst = []
    for num in range(2,101):
        if all(num%i!=0 for i in range(2,num)):
            lst.append(num)
    sq_list = []
    for i in lst:
        a = i*i
        sq_list.append(a)
    count = 0
    for i in test:
        for k in sq_list:
            if i> k:
                count += 1
        fin_out.append(count)
        count = 0
    return print(*fin_out, sep ="\n")

Triprime_checker(test)