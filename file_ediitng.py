path = "C://Users//NELSON JOSEPH//Desktop//Cash.txt"
file1 = open(path)
lst = []
for line in file1.readlines():
    a, b = line.split(": ")
    lst.append(b)
sum = 0
lst1 =["Bristo", "Jerin"]
for i, j in enumerate(lst, 1):
    name, amount = j.split()
    sum += int(amount)
    if name in lst1:
        print("{}  {} - {} S&f ={} P&L = {}".format(i, name, amount, 1200-int(amount), 300))
    else:
        print("{}  {} - {} S&f ={} P&L = {}".format(i, name, amount, 1200-int(amount), 600))
print("Total =", sum)
print("Remaining to pay at hotel =", 12*1200-sum)
sF, ptrl, lq = 700/11, 300/11, 300/9
print("Extra expense without pindu:- \n\nFor S&f= +{}\nFor Petrol= +{}\nFor liquor= +{}".format(sF, ptrl, lq))
print("Extra money Alcoholics = {}\nExtra money Non-Alcholics = {}".format(round(sF+ptrl+lq,2), round(sF+ptrl,2)))
