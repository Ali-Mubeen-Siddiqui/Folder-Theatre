from customtkinter import *
from tkinter import *
import json
from . import statusBar
from . import navBar


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("644x433")
        self.minsize(444, 233)
        self.title("Folder Theatre")
        self.loadComponents()
        
        self.loadTheme()

    def setTheme(self,theme):
        # applies theme
        self._set_appearance_mode(theme)

    def loadTheme(self):
        try:
            with open("components/settings.json", "r") as file:
                setting = json.load(file)
            theme = setting["themes"]["current"]
            self.setTheme(theme)
        except Exception as e:
            self.setTheme("dark")

    def nav(self,sb):
        nav = navBar.Navbar(self,sb)
        self.config(menu=nav)


    def loadComponents(self):
        sb = self.statusbar()
        self.nav(sb)
            
    def statusbar(self):
        sb = statusBar.StatusBar(self)
        
        sb.pack(fill=X, side=BOTTOM)
        return sb



