import os
import pandas as pd
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_dir)

files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)
    all_data.append(df)

df_all = pd.concat(all_data)

result = df_all.groupby("area")["price"].sum().reset_index()

result.to_excel("all_total.xlsx", index=False)

print("完了！")

##all_total.xlsx が作成されます

## 想定用途

- 売上管理
- データ整理
- 業務の自動化

## 制作者

inari-auto