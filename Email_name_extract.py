N = int(input())
lst = []
for _ in range(N):
    Name, Email = input().split()
    if Email.endswith("@gmail.com"):
        lst.append(Name)
    else:
        pass
lst.sort()
# print("\n".join(map(str, lst)))
print(*lst, sep = '\n')
