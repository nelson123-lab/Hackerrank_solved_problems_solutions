import re

data = "GeeksforGeeks, is_an-awesome ! website"
email = "<dexter@hotmail.com>"
res1 = re.split(', |_|-|!', data)
res = re.split('<|@|\.|>',email)
print(res)