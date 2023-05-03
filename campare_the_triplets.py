def compareTriplets(a, b):
    A=0
    B=0
    p=0
    for i in range(len(a)):
        for n in range(len(b)):
            if i==p and n==p:
                if a[i]>b[n]:
                    A += 1
                elif a[i]<b[n]:
                    B += 1
                else:
                    pass
                p=p+1
    return A,B

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = compareTriplets(a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

        fptr.close()
