try:
    hours = float(input("Enter hours"))
    rate = float(input("Enter rate"))
except:
    print("Enter numbers only")
    quit()
if hours < 40:
    h = hours*rate
    print("pay: "+ str(h))
else:
    r = 40*rate + ((hours-40)*rate*1.5)
    print("pay: "+ str(r))
