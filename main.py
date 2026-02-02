import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_dir)

# CSV読み込み
df = pd.read_csv("data/input.csv")

# 日付変換
df["date"] = pd.to_datetime(df["date"])

# 金額フィルター（2000円以上）
df = df[df["price"] >= 2000]

# 集計
summary = (
    df.groupby("area")["price"]
    .sum()
    .reset_index()
    .rename(columns={"price": "total_price"})
)

# Excel出力
summary.to_excel("result.xlsx", index=False)

print("完了！ result.xlsx を作成しました")