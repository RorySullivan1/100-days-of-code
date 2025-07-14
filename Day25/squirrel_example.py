import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df2 = df.groupby("Primary Fur Color").count()["X"]
df2.rename({"X":"count"})
print(df2)
