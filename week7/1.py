import tkinter as tk
import threading
import time

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")
        
        self.running = False
        
        # UI Elements
        self.lbl_instruction = tk.Label(root, text="Enter Seconds:")
        self.lbl_instruction.pack(pady=5)
        
        self.entry_seconds = tk.Entry(root)
        self.entry_seconds.pack(pady=5)
        
        self.lbl_display = tk.Label(root, text="00:00", font=("Arial", 24))
        self.lbl_display.pack(pady=20)
        
        self.btn_start = tk.Button(root, text="Start", command=self.start_thread)
        self.btn_start.pack(side=tk.LEFT, padx=40)
        
        self.btn_stop = tk.Button(root, text="Stop", command=self.stop_timer)
        self.btn_stop.pack(side=tk.RIGHT, padx=40)

    def start_thread(self):
        if not self.running:
            self.running = True
            # Get value from entry
            try:
                seconds = int(self.entry_seconds.get())
                t = threading.Thread(target=self.run_timer, args=(seconds,))
                t.start()
            except ValueError:
                self.lbl_display.config(text="Error!")

    def run_timer(self, seconds):
        while seconds >= 0 and self.running:
            # Update UI from thread
            mins, secs = divmod(seconds, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            self.lbl_display.config(text=time_format)
            
            time.sleep(1)
            seconds -= 1
        
        if self.running:
            self.lbl_display.config(text="Time's up!")
            self.running = False

    def stop_timer(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
