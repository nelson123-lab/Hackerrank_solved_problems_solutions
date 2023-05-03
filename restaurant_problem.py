def restaurant(single_tables, double_tables, visitors):
    pos = single_tables
    pod = double_tables *2
    count = 0
    for i in visitors:          #[1,1,2,1]
        if i == 1:
            if pos-i < 0:       #
                if pod-1< 0:
                    count += i
                else:
                    pod -= 1     #pod =1
            else:
                pos -= 1         #pos = 0
        else:
            if pod-2 < 0:
                count += i
            else:
                pod -= i
                
    return count 