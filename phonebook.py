"""
details = input("enter details")
def phone_book(details):
    p = details.split()
    name = p[0]
    no = p[1]
    return "{} = {}".format(name,str(no))
print(phone_book(details))
"""
import sys

n = int(sys.stdin.readline().strip())

phone_book = dict()

for i in range(n):
    entry = sys.stdin.readline().strip().split(' ')
    phone_book[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    phone_no = phone_book.get(query)
    if phone_no:
        print(query+ "="+ phone_no)
    else:
        print("Not found")
    query = sys.stdin.readline().strip()
