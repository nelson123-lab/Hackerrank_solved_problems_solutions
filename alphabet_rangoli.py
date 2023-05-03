def print_rangoli(size):
    alpha = "a"
    alpha_list=[]
    #to make an alphabet list
    for i in range(0,26):
        alpha_list.append(alpha)
        alpha = chr(ord(alpha)+1)
    size_list = alpha_list[0:n]
    b=''
    for i in size_list:
        b=b+"-"+i
    center_element = b[::-1]+b[3:]
    #center element is having the maximum length
    width = len(center_element)
    #4 elemnts are removed in each iteration in my observation
    a = center_element[0:width//2]+center_element[(width//2+4):]
    lower_half =[]
    for i in range(1,n):
        lower_half.append(a.center(width,"-"))
        a= a[0:len(a)//2]+a[(len(a)//2+4):]
    # there is a test case that size = 1 we have to get output "a"
    if n>1:
        #below print is print the ouput in line by line in reverse order
        print(*lower_half[::-1],sep ="\n",end="")
        print("\n" + center_element)
        #print line by line(does same as 1st print statement just to know that there are several ways to do this when i go through this  again) in the normal order
        print("\n".join(lower_half))
    else:
            print(size_list[0])
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
