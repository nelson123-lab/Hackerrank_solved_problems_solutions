# import time


# def prime_no(num):
#     if num<2:
#         return False
#     else:
#         for i in range(2, num//2+1):
#             if num % i == 0:
#                 return False
#         return True
# # range(2,2) is 0 and x modulus of 0 is undefined so num % i != 0

# def Prime_under_num(n):
#     a = [2]
#     if n <2:
#         print("None")
#     elif n==2:
#         print(2)
#     else:
#         for i in range(3, n+1, 2):   
#             if prime_no(i):
#                 a.append(i)
#         print(a)
#Total Running time = 0.001 seconds # 100
#Total Running time = 0.004 seconds #1000
#Total Running time = 0.224 seconds #10000
#Total Running time = 12.857 seconds #100000


def Prime_under_num(n):
    a = [2]
    if n <2:
        print("None")
    elif n==2:
        print(2)
    else:
        for i in range(3, n+1, 2):   
            if n%i ==0:
                pass
            else:
                a.append(i)
        print(a)

# Total Running time = 2.75935 seconds #n = 100
# Total Running time = 2.86332 seconds #n = 1000
# Total Running time = 4.59884 seconds #n = 10000
# Total Running time = 8.55057 seconds #n = 100000
if __name__ == "__main__" :
    n = int(input())
    start_time = time.time()
    Prime_under_num(n)
    print("Total Running time = {:.5f} seconds".format(time.time() - start_time))


