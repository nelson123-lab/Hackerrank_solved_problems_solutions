#find something from a data
data1 = "hello hi nice to meet you*3385795 this my no"
data2 = "hello hi nice to meet you*7898887 this my no"
data3 = "hello hi nice to meet you*7080780 this my no"
for num in [data1,data2,data3]:
    finder = num.find("*")
    finder2 =num.find(' ',finder)
    no=num[finder+1 : finder2]
    print(no)
