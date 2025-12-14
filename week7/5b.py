import tkinter as tk
import threading
import queue
import time

class JobDispatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Dispatcher")
        self.root.geometry("400x400")
        
        self.job_queue = queue.Queue()
        self.result_queue = queue.Queue()
        
        # Start Worker Thread immediately (Daemon means it dies when app closes)
        self.worker_thread = threading.Thread(target=self.worker_task, daemon=True)
        self.worker_thread.start()

        # UI
        tk.Label(root, text="Job Input (Number):").pack(pady=5)
        self.entry_job = tk.Entry(root)
        self.entry_job.pack(pady=5)
        
        self.btn_add = tk.Button(root, text="Add Job (Multiply by 2)", command=self.add_job)
        self.btn_add.pack(pady=10)
        
        tk.Label(root, text="Completed Jobs:").pack(pady=5)
        self.result_list = tk.Listbox(root)
        self.result_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Start checking results
        self.update_ui()

    def add_job(self):
        try:
            num = int(self.entry_job.get())
            self.job_queue.put(num)
            self.entry_job.delete(0, tk.END)
            print(f"Job added: {num}")
        except ValueError:
            print("Please enter a valid number")

    def worker_task(self):
        while True:
            # Wait for job
            job = self.job_queue.get()
            
            # Process job (simulate work)
            time.sleep(1) 
            result = job * 2 # Example: Multiply by 2
            
            # Send to result queue
            self.result_queue.put(f"Job: {job} -> Result: {result}")
            self.job_queue.task_done()

    def update_ui(self):
        try:
            while True:
                res = self.result_queue.get_nowait()
                self.result_list.insert(tk.END, res)
        except queue.Empty:
            pass
        
        # Check again after 500ms
        self.root.after(500, self.update_ui)

if __name__ == "__main__":
    root = tk.Tk()
    app = JobDispatcherApp(root)
    root.mainloop()
