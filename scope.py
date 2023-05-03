"""
from itertools import permutations
maximumDifference =0
class Difference:
    def __init__(self,elements):
        self.elements = elements
    def computeDifference(self):
        global maximumDifference
        p = list(permutations(self.elements, 2))
        for i in p:
            q = abs(i[0]-i[1])
            if q > maximumDifference:
                maximumDifference = q
        return str(q)

a = int(input())
list1 = [int(e) for e in input().split(" ")]
diff = Difference(list1)
diff.computeDifference()
print(maximumDifference)
"""
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0 #instance variable of class
    def computeDifference(self):
        self.maximumDifference = abs(max(a)-min(a))

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
