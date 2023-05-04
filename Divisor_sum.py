while True:
    a = int(input("Enter the no?"))
    divisor_list = []
    for i in range(1, a+1):
        if a % i ==0:
            divisor_list.append(i)
    print(sum(divisor_list))
    if a == 1:
        break
