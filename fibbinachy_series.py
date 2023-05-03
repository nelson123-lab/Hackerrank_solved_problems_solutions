# """Recursive method"""
# def fib_2(n,memo):
#   if memo[n] is not None:
#     return memo[n]
#   if n==1 or n==2:
#     result = 1
#   else:
#     result = fib_2(n-1, memo) + fib_2(n-2, memo)
#   memo[n] = result
#   return result
#
# def fib_memo(n):
#     memo =[None]*(n+1)
#     return fib_2(n, memo)

"""Simple method"""
def fib(n):
    x1, x2 = 1, 1
    while n > 1:
        x1, x2 = x2, x1 + x2
        n -= 1
    print(x1)
    return x1

print(fib(5))
# print(fib_memo(2))
