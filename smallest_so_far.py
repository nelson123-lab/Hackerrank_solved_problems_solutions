smallest=None
for value in [4,6,22,65,12,11,89,99,78,2,1]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest=value
    print('Running test cases = {}'.format(value))
print("Smallest is ",smallest)
