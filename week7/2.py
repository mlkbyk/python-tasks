import tkinter as tk
import threading
import time
import random

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot")
        self.root.geometry("400x500")

        # Chat Area
        self.chat_area = tk.Text(root, state='disabled', width=50, height=20)
        self.chat_area.pack(pady=10, padx=10)

        # Entry Area
        self.entry_msg = tk.Entry(root, width=40)
        self.entry_msg.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_send = tk.Button(root, text="Send", command=self.send_message)
        self.btn_send.pack(side=tk.RIGHT, padx=10, pady=10)

    def send_message(self):
        user_msg = self.entry_msg.get()
        if user_msg:
            self.display_message("You: " + user_msg + "\n")
            self.entry_msg.delete(0, tk.END)
            
            # Start bot thread
            t = threading.Thread(target=self.bot_response)
            t.start()

    def bot_response(self):
        # Simulate thinking time
        time.sleep(1.5)
        
        responses = ["Hello!", "I am a thread bot.", "Nice to meet you.", "Python is cool."]
        bot_msg = random.choice(responses)
        
        self.display_message("Bot: " + bot_msg + "\n")

    def display_message(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, msg)
        self.chat_area.see(tk.END) # Scroll to bottom
        self.chat_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
