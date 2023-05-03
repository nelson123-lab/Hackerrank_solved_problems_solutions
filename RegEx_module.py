import re

text = "X-DSPAM-Confidence:    0.847 5"
x=re.search("^X.*5$",text)
if x:
    print("match")
