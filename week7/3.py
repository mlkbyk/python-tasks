import tkinter as tk
from tkinter import filedialog
import threading
import time
# Note: Usually we use PIL (Pillow) for images, but for simplicity 
# we use standard PhotoImage (supports PNG/GIF)
import os

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("500x400")

        self.btn_open = tk.Button(root, text="Open Image", command=self.start_loading_thread)
        self.btn_open.pack(pady=20)

        self.lbl_status = tk.Label(root, text="No image loaded", fg="gray")
        self.lbl_status.pack()

        self.lbl_image = tk.Label(root)
        self.lbl_image.pack(pady=20)

    def start_loading_thread(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.gif")])
        if file_path:
            # Start thread
            t = threading.Thread(target=self.load_image, args=(file_path,))
            t.start()

    def load_image(self, file_path):
        self.lbl_status.config(text="Loading... Please wait...")
        self.btn_open.config(state='disabled')
        
        # Simulate heavy loading task
        time.sleep(2) 
        
        try:
            # Load image
            self.img = tk.PhotoImage(file=file_path)
            
            # Update UI (Note: In complex apps use queue, here simple config works)
            self.lbl_image.config(image=self.img)
            self.lbl_status.config(text="Loaded: " + os.path.basename(file_path))
        except Exception as e:
            self.lbl_status.config(text="Error loading image")
            print(e)
            
        self.btn_open.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()
