
# def prime(no):
#     if no<2: return False
#     elif no == 2: return True
#     elif no %2 == 0: return False
#     else:
#         for i in range(3, int(no**0.5), 2):
#             if no%i == 0:
#                 return False
#         return True


# def count_primes(N):
#     count = 1
#     if N < 2: return 0
#     for i in range(3, N, 2):
#         if prime(i):
#             count +=1
#         else:
#             pass
#     return count

# print(count_primes(20))
        
# Optimal solution

def countPrimes(n):
        isPrime = [True] * n # Generates a list of True for the number till n
        isPrime[:2] = [False, False] # Makes the first 2 positions as False 0 and 1.
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i: n: i] = [False] * len(isPrime[i * i: n: i]) #Converts all multiples of prime numbers as False, 
        return sum(isPrime)
print(countPrimes(10))