def countSubarrays(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]

    odd_count = 0
    for i in range(n):
        for j in range(i, n):
            if (prefix[j+1] - prefix[i]) % 2 == 1:
                odd_count += 1

    return odd_count

print(countSubarrays([1, 3, 5]))

# Most optimal solution so far
def numOfSubarrays(self, arr: List[int]) -> int:
        s = [1,0]
        mod = 10**9 +7

        r, run = 0,0
        for a in arr:
            run += a
            run %= 2

            r += s[(run+1)%2]
            s[run] += 1
        return r % mod