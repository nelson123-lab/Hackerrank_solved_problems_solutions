import pandas as pd
import numpy as np
# to create a DataFrame using array
df= pd.DataFrame(np.random.randn(3,3))
print(df)

# to create a dataframe using dictonary
df3 = pd.DataFrame({"E": np.array([4]*5 ,dtype = "int32"), "Day" : 2})
print(df3)

"""
for url
url = "djkfsjdkf"
df = pd.read_csv(url, header = None)
"""
