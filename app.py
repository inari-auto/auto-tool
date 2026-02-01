import tkinter as tk
import subprocess

def run():
    subprocess.run(["python3", "multi.py"])

root = tk.Tk()
root.title("自動集計ツール")

btn = tk.Button(root, text="実行", command=run)
btn.pack(padx=30, pady=30)

root.mainloop()