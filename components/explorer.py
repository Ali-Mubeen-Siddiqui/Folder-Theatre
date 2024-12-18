from customtkinter import *

class Explorer(CTkFrame):
    def __init__(self,root,statusKey,fg):
        self.root = root
        self.statusKey = statusKey
        self.fg = fg
        super().__init__(master=self.root,fg_color=self.fg)
        self.pack()