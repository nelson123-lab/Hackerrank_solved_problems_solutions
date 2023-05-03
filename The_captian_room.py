# Enter your code here. Read input from STDIN. Print output to STDOUT
element = int(input())
lst = list(map(int, input().split()))



""" All test cases passed"""
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
a = set() 
b = set()
for i in lst:
    if i in a:
        b.add(i)
    else:
        a.add(i)
print(*(a-b))

""" Set function uses a four loop to convert list to a set"""
""" Takes more time to process and it fails to correct all test cases"""
# a = [] 
# b = set()
# for i in lst:
#     if i in a:
#         b.add(i)
#     else:
#         a.append(i)
# print(*(set(a)-b))

""" All test cases passed"""
# a = set() 
# b = set()
# for i in lst:
#     if i not in a:
#         a.add(i)
#     else:
#         b.add(i)
# print(*(a-b))

""" Error due to timeout"""
# a = [] 
# b = set()
# for i in lst:
#     if i not in a:
#         a.append(i)
#     else:
#         b.add(i)
# print(*(set(a)-b))


""" 5 test cases correct """
# a = [] 
# b = [] 
# for i in lst:
#     if i not in a:
#         a.append(i)
#     else:
#         b.append(i)
# for i in a:
#     if i not in b:
#         print(i)

""" 3 test cases correct """
# A = set(lst)
# for i in A:
#     if lst.count(i) ==1:
#         print(i)

""" 3 test cases correct """
# a = [] 
# b = [] 
# for i in lst:
#     if i not in a:
#         a.append(i)
#     else:
#         b.append(i)
# for i in a:
#     if b.count(i) ==0:
#         print(i)

""" 3 test cases correct """      
# for i in lst:
#     if lst.count(i) == 1:
#         print(i)

""" 3 test cases correct """
# dict1 = {p: lst.count(p) for p in lst}

# print(list(dict1.keys())[list(dict1.values()).index(1)])

""" 3 test cases correct """
# Keymax = min(zip(dict1.values(), dict1.keys()))[1]
# print(Keymax)

""" 2 test cases correct """
# for key, values in dict1.items():
#     if values == 1:
#         print(key)
# for key, values in dict1.items():
#     if values != element:
#         print(key)
