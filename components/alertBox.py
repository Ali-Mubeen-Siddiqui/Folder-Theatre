from tkinter import messagebox
class Alert:
    def __init__(self, root, text,head):
        self.root = root
        self.text = text
        self.head = head

    def show(self):
        messagebox.showinfo(self.head, self.text, parent=self.root,)