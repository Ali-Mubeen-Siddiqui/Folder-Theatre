from customtkinter import *
import json


class Area(CTkFrame):
    def __init__(self,root,theme,statusKey):
        self.root = root
        self.theme = theme
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


        super().__init__(master=self.root,height=455,fg_color=self.fg)
        
        self.pack(fill=BOTH,expand=True)
        

    def loadThemeArea(self):
        with open("components/settings.json","r") as file:
            settings = json.load(file)
            if settings["themes"]["current"] == "system":
                if self.root.cget("bg") == "light":
                    self.fg = "white"
                else:
                    self.fg = "grey10"
                

            else:
                if settings["themes"]["current"] == "light":
                    self.fg = "white"
                else:
                    self.fg = "grey10"

            self.configure(fg_color=self.fg)
            
            

    
