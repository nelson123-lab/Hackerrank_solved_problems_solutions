cube = lambda x: x*x*x # complete the lambda function

def fibonacci(n):
    lst =[0]
    a,b = 0,1
    while n > 1:
        a,b = b, a+b
        lst.append(a)
        n -= 1
    return lst

    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
