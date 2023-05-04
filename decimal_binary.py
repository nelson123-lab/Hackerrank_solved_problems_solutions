n = int(input())
current_con = 0
max_con = 0
while n>0:
    remainder = n % 2
    if remainder == 1:
        current_con +=1
        if current_con > max_con:
            max_con = current_con
    else:
        current_con = 0
    n = n//2
print(max_con)
