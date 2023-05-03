def aVeryBigSum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum
n= int(input())
arr= list(map(int, input().rstrip().split()))
print(aVeryBigSum(arr))
