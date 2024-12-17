from customtkinter import *
from tkinter import *
import json

from navBar import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("644x433")
        self.minsize(444, 233)
        self.title("Folder Theatre")
        nav = Navbar(self)
        self.config(menu=nav)
        self.loadTheme()

    def setTheme(self,theme):
        # applies theme
        self._set_appearance_mode(theme)

    def loadTheme(self):
        try:
            with open("settings.json", "r") as file:
                setting = json.load(file)
            theme = setting["themes"]["current"]
            self.setTheme(theme)
        except Exception as e:
            self.setTheme("dark")
            



