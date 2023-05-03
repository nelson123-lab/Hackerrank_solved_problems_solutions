hours = input("Enter hours")
rate = input("Enter rate")
if hours.isdigit() & rate.isdigit():
    if int(hours) < 40:
      h = int(hours)*int(rate)
      print("pay: "+ str(h))
    else:
      r = 40*rate + ((hours-40)*rate*1.5)
      print("pay: "+ str(r))
else:
    print("Enter numbers only")
