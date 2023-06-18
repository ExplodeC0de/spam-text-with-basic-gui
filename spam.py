import pyautogui
import tkinter as tk
from time import sleep
import threading

class TypingProgram:
    def __init__(self, text):
        self.text = text
        self.is_running = False
        self.root = tk.Tk()
        self.root.title("Typing Program")
        self.label = tk.Label(self.root, text="Press Start to begin typing")
        self.label.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_typing)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_typing, state=tk.DISABLED)
        self.stop_button.pack()

    def start_typing(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.label.config(text="Typing...")
        threading.Thread(target=self.type_text).start()

    def type_text(self):
        while self.is_running:
            pyautogui.typewrite(self.text)
            pyautogui.press("enter")
            sleep(2)

    def stop_typing(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.label.config(text="Typing stopped")

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    program = TypingProgram("Hello, you are a victim of this spamming script!")
    program.run()
