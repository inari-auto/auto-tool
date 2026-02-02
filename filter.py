import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_dir)

df = pd.read_csv("data/input.csv")

df["date"] = pd.to_datetime(df["date"])

target_month = "2026-01"
target_area = "Tokyo"

df = df[df["date"].dt.to_period("M") == target_month]
df = df[df["area"] == target_area]

result = (
    df.groupby("area")["price"]
    .sum()
    .reset_index()
)

result.to_excel("filter_result.xlsx", index=False)

print("完了！ filter_result.xlsx を作成しました")