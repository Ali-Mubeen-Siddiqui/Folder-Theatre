from customtkinter import *
from tkinter import *
import json
from . import explorer,extra

class Area(PanedWindow):
    def __init__(self,root,theme,statusKey):
        
        self.root = root
        self.theme = theme
        self.statusKey = statusKey
        with open("components/settings.json","r") as file:
            settings = json.load(file)
            if settings["themes"]["current"] == "system":
                if self.root.cget("bg") == "SystemButtonFace":
                    self.fg = "white"
                else:
                    self.fg = "grey10"
            else:
                self.fg = self.theme
            
        if self.fg == "light":
            self.fg = "white"
        else:
            self.fg = "grey10"
        super().__init__(master=self.root,height=455,orient=HORIZONTAL)
        
        self.pack(fill=BOTH,expand=True)
        self.loadArea()
        

    def loadThemeArea(self):
        with open("components/settings.json","r") as file:
            settings = json.load(file)
            if settings["themes"]["current"] == "system":
                if self.root.cget("bg") == "SystemButtonFace":
                    self.fg = "white"
                else:
                    self.fg = "grey10"
            else:
                self.fg = settings["themes"]["current"]
                if self.fg == "light":
                    self.fg = "white"
                else:
                    self.fg = "grey10"

            self.configure(bg=self.fg)
            self.panel1.configure(fg_color=self.fg)
            self.panel2.configure(fg_color=self.fg)
            # self.update_idletasks()


    def loadArea(self):
        self.panel1 = explorer.Explorer(self,self.statusKey,self.fg)
        self.panel2 = extra.Extra(self,self.statusKey,self.fg)

        self.add(self.panel1)
        self.add(self.panel2)