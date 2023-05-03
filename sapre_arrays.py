string_no = int(input())
string = []
for i in range(string_no):
    string1 = input()
    string.append(string1)
qurie_no = int(input())
queries = []
for i in range(qurie_no):
    quire1 = input()
    queries.append(quire1)
out={}
for i in queries:
    if  i in string:
        out[i] = string.count(i)
    else:
        out[i] = 0
print("\n".join([str(i) for i in out.values()]))
