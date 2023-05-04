import re

text = "X-DSPAM-Confidence:    0.8475"
x=re.search("^X.*5$",text)
if x:
    print("match")
