score = input("Enter numbers for grades")
try:
    sc = float(score)
except:
    print("Enter numbers only")
    quit()
if sc <0.0 or sc>1.0:
    print("Enter values in the desired range")
else:
    if sc >= 0.9:
         print("A")
    elif sc >= 0.8:
        print("B")
    elif sc >= 0.7:
        print("C")
    elif sc >= 0.6:
        print("D")
    else:
        print("F")
