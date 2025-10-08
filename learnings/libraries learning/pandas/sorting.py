import pandas as pd

data = {
   "Time": [1,2,3,4,5],
    "Value": [10,None,30,None,40]
}

df = pd.DataFrame(data)
print(df)
print("Sorted by time:")
df.sort_values(by="Time",ascending=True,inplace=True,ignore_index=True)
print(df)
