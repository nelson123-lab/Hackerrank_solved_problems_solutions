import math

def is_prime(n):
    if n <1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n)+1):
        if n%i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    p= int(input())
    if is_prime(p):
        print("Prime")
    else:
        print("Not prime")
