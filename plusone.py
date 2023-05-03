def plus_one(list1):
    a = len(list1)-1
    no = 0
    for idx, ele in enumerate(list1):
        no = no + ele*10**(a-idx)
    return [int(i) for i in str(no + 1)]

def plus_one_str(list1):
    a = list(map(str, list1))
    return list(str(int("".join(a))+1))
list1 = [1, 2, 3, 4, 5, 6, 7]
print(plus_one(list1))

