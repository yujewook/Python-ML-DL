import numpy as np
import pandas as pd

df = pd.DataFrame(
    [["you",89,92,95],
     ["kim",46,np.NaN,65],
     ["lee",32,np.NaN,30],
     ["park",np.NaN,np.NaN,30],
     ["kang",np.NaN,np.NaN,np.NaN]
     ] , columns=["name","kor","eng","mat"]
    
    )

print(df.info())
print(df.describe())
print(df.count(axis=1))
print(df.sum)
print(df[["kor","eng","mat"]].sum(axis=1))
print(df)