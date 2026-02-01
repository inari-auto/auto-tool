import pandas as pd

df = pd.read_csv("input.csv")

df["date"] = pd.to_datetime(df["date"])

df = df[df["price"] >= 2000]

summary = df.groupby("area")["price"].sum()

summary.to_excel("result.xlsx")

print("完了！")
