import calendar

input1 = list(map(int, input().split(" ")))
month, day, year = input1[0], input1[1], input1[2]
c = calendar.weekday(year, month, day)
days = ["MONDAY", "TUESDAY", "WEDNESDAY","THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(days[c])
