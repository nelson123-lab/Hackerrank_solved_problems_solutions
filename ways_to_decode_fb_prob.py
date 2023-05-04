def helper(data, k):
    if k ==0:
        return 1
    s = len(data) -k
    if data[s] =='0':
        return 0
    result = helper(data, k-1)
    if k >=2 and int(data[s:s+2])<=26:
        result += helper(data, k-2)
    return result

def num_ways(data):
    return helper(data, len(data))
#https://youtu.be/qli-JCrSwuk?list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev
p = '2626'
print(num_ways(p))
"""
fails when same no repeats
"""
