import pandas as pd

data = {
 "Name": ["Jonash", "Aayush", "Jon","Jane","Mane","Lane"],
 "Age": [20,49,26,16,49,56],
 "Salary": [25000,13000,4500,6310,78066,78945]
}

df = pd.DataFrame(data)
print(df)

grouped_by_age=df.groupby("Age")["Salary"].sum()
print(grouped_by_age)

