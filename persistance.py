# Normal method

def persistance(num):
    counter=0
    while num>9:
        counter+=1
        num_str=str(num)
        total=1
        for i in num_str:
            total=total* int(i)
        num=total
    print (counter)

#Using recursion

def persistence(num):
    if num < 10:
        return 0 # Only one digit. Can't iterate over it
    num_str = str(num)
    total = 1
    for i in num_str:
        total = total * int(i)
    return 1 + persistence(total) # We do 1 + because we just did an iteration



print(persistance(39))