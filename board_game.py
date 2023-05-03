def matrix(n, m):
    cell_val = []
    for i in range(n):
        rows = []
        for j in range(m):
            val = (i+1)*(j+1)
            rows.append(val)
        cell_val.append(rows)
    return cell_val
# n, m = 3, 4
queries = [[0], [1,2], [0], [2,1], [0], [1,1], [0]]
n, m = 3,4
matrix = matrix(n, m)
res = []
for i in queries:
    if i[0] == 0:

    elif i[0] == 1:

    elif i[0] == 2:

        a = []


# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     # queries = input()
#     print(matrix(n, m))
#     for i in queries:
#         if i == [0]:
#             print(min(solution(n, m).flatten()))
#         else:
#             print("something")
