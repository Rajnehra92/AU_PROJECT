
import tkinter as tk
from tkinter import filedialog, scrolledtext

class Linecounter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.line = []
        self.ip_add = []

    def read(self):
        with open(self.file_name, "r") as f:
            self.line = f.readlines()

    def fetch_ip_add(self):
        if not self.line:
            self.read()
        self.ip_add = [line.split(" ")[0] for line in self.line]
        return self.ip_add

    def ip_add_20(self):
        if not self.ip_add:
            self.fetch_ip_add()
        return [ip for ip in self.ip_add if int(ip.split(".")[0]) < 20]

    def ratio(self):
        total_ips = self.fetch_ip_add()
        less_20_ips = self.ip_add_20()
        return len(less_20_ips) / len(total_ips) if total_ips else 0


# ---- Tkinter GUI ----
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        lc = Linecounter(file_path)
        lc.read()
        first_line = lc.line[0] if lc.line else "No lines found."
        all_ips = lc.fetch_ip_add()
        less_20 = lc.ip_add_20()
        ratio_val = lc.ratio()

        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, f"First line:\n{first_line}\n")
        text_output.insert(tk.END, f"\nAll IPs:\n{all_ips}\n")
        text_output.insert(tk.END, f"\nIPs with first number < 20:\n{less_20}\n")
        text_output.insert(tk.END, f"\nRatio: {ratio_val:.2f}\n")


# Main Window
root = tk.Tk()
root.title("IP Log Analyzer")

# Button to load file
btn_load = tk.Button(root, text="Load Log File", command=load_file)
btn_load.pack(pady=10)

# Text box to show results
text_output = scrolledtext.ScrolledText(root, width=100, height=25)
text_output.pack(padx=10, pady=10)

root.mainloop()
