import pandas as pd

data = {
    "Time": [1,2,3,4,5],
    "Value": [10,None,30,None,40]
}

df = pd.DataFrame(data)
print(df)

# print("Mean used for missing datas:")
# df["Value"].fillna(df["Value"].mean(), inplace=True)
# print(df)

print("Interpolation used:")
df["Value"].interpolate(method="linear",inplace=True)
print(df)
