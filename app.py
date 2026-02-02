import tkinter as tk
import subprocess
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

def run_main():
    subprocess.run(["python3", os.path.join(base_dir, "main.py")])

def run_multi():
    subprocess.run(["python3", os.path.join(base_dir, "multi.py")])

def run_filter():
    subprocess.run(["python3", os.path.join(base_dir, "filter.py")])

root = tk.Tk()
root.title("CSV自動集計ツール")

tk.Label(root, text="処理を選択してください").pack(pady=10)

tk.Button(root, text="金額フィルター集計", width=25, command=run_main).pack(pady=5)
tk.Button(root, text="一括集計（全CSV）", width=25, command=run_multi).pack(pady=5)
tk.Button(root, text="月・エリア集計", width=25, command=run_filter).pack(pady=5)

root.mainloop()