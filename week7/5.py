import tkinter as tk
import threading
import queue
import time

class ProducerConsumerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Producer - Consumer")
        self.root.geometry("300x400")
        
        self.data_queue = queue.Queue()
        self.producer_running = False

        self.btn_start = tk.Button(root, text="Start Producer", command=self.start_producer)
        self.btn_start.pack(pady=10)

        self.btn_stop = tk.Button(root, text="Stop Producer", command=self.stop_producer)
        self.btn_stop.pack(pady=5)

        self.lbl_info = tk.Label(root, text="Generated Numbers:")
        self.lbl_info.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Start the consumer loop (GUI Check)
        self.check_queue()

    def start_producer(self):
        if not self.producer_running:
            self.producer_running = True
            t = threading.Thread(target=self.producer_task)
            t.start()

    def stop_producer(self):
        self.producer_running = False

    def producer_task(self):
        counter = 1
        while self.producer_running and counter <= 100:
            time.sleep(0.5) # Generate number every 0.5 sec
            self.data_queue.put(counter)
            counter += 1

    def check_queue(self):
        # CONSUMER (Main Thread)
        try:
            while True:
                # Get data without blocking
                number = self.data_queue.get_nowait()
                self.listbox.insert(tk.END, f"Number received: {number}")
                self.listbox.see(tk.END)
        except queue.Empty:
            pass
        
        # Check again after 200ms
        self.root.after(200, self.check_queue)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProducerConsumerApp(root)
    root.mainloop()
