from tkinter import messagebox
class Alert:
    def __init__(self, root, text):
        self.root = root
        self.text = text

    def show(self):
        messagebox.showinfo("Alert", self.text, parent=self.root)