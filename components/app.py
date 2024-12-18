from customtkinter import *
from tkinter import *
import json
from . import statusBar
from . import navBar
from . import views
from . import area


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("644x433")
        self.minsize(444, 233)
        self.title("Folder Theatre")
        self.loadTheme()
        self.loadComponents()
        

    def setTheme(self,theme):
        self.theme = theme
        # applies theme
        self._set_appearance_mode(self.theme)

    def loadTheme(self):
        try:
            with open("components/settings.json", "r") as file:
                setting = json.load(file)
            theme = setting["themes"]["current"]
            self.setTheme(theme)
        except Exception as e:
            self.setTheme("dark")

    def nav(self,sb,erKey):
        nav = navBar.Navbar(self,sb,erKey)
        self.config(menu=nav)


    def loadComponents(self):
        sb = self.statusbar()
        self.loadviews(sb)
        la = self.loadarea(sb)
        self.nav(sb,la)
            
    def statusbar(self):
        sb = statusBar.StatusBar(self)
        
        sb.pack(fill=X, side=BOTTOM)
        return sb
    
    def loadviews(self,sb):
        myview = views.view(self,sb)

    def loadarea(self,sb):
        fArea = area.Area(self,self.theme,sb)
        return fArea
        




