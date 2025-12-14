import tkinter as tk
from tkinter import ttk
import threading
import time
import random

class MultiProgressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Progress Simulator")
        self.root.geometry("400x300")

        self.btn_start = tk.Button(root, text="Start All", command=self.start_threads)
        self.btn_start.pack(pady=10)
        
        self.btn_reset = tk.Button(root, text="Reset", command=self.reset_bars)
        self.btn_reset.pack(pady=5)

        # Progress Bars
        self.lbl1 = tk.Label(root, text="Task 1")
        self.lbl1.pack()
        self.prog1 = ttk.Progressbar(root, length=300, mode='determinate')
        self.prog1.pack(pady=5)

        self.lbl2 = tk.Label(root, text="Task 2")
        self.lbl2.pack()
        self.prog2 = ttk.Progressbar(root, length=300, mode='determinate')
        self.prog2.pack(pady=5)

        self.lbl3 = tk.Label(root, text="Task 3")
        self.lbl3.pack()
        self.prog3 = ttk.Progressbar(root, length=300, mode='determinate')
        self.prog3.pack(pady=5)

    def start_threads(self):
        t1 = threading.Thread(target=self.run_bar, args=(self.prog1,))
        t2 = threading.Thread(target=self.run_bar, args=(self.prog2,))
        t3 = threading.Thread(target=self.run_bar, args=(self.prog3,))
        
        t1.start()
        t2.start()
        t3.start()

    def run_bar(self, bar):
        for i in range(101):
            time.sleep(random.uniform(0.02, 0.1)) # Random speed
            bar['value'] = i
            # Usually we use root.update_idletasks() or after, but this works for simple visuals

    def reset_bars(self):
        self.prog1['value'] = 0
        self.prog2['value'] = 0
        self.prog3['value'] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiProgressApp(root)
    root.mainloop()
