def subSet_tester(A, B):
    for i in A:
        if i not in B:
            return False
    return True




test_case = int(input())
for i in range(test_case):
    set_A = int(input())
    A = set(map(int, input().split()))
    set_B = int(input())
    B = set(map(int, input().split()))
    print(subSet_tester(A, B))