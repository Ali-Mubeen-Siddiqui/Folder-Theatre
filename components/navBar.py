from tkinter import *
import json
from . import systemOT
from . import openClose
from . import alertBox


class Navbar(Menu):
    def __init__(self,root,statusKey):
        super().__init__()
        self.loadWidget(root,statusKey)
        
        

    def loadWidget(self,root,statusKey):
        self.folderWidget(root,statusKey)
        self.themesWidget(root)
        self.loadVersion(root)
        
    def folderWidget(self,root,statusKey):
        folder_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Folder", menu=folder_menu)
        folder_menu.add_command(label="Open", accelerator="Ctrl+O", command = lambda : openClose.open_folder(root,statusKey))
        folder_menu.add_command(label="Close", accelerator="Ctrl+C")
        

    def themesWidget(self,root):
        themes_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Themes", menu=themes_menu)
        themes_menu.add_command(label="Light",command= lambda : systemOT.changetheme("light",root))
        themes_menu.add_command(label="Dark",command= lambda : systemOT.changetheme("dark",root))
        themes_menu.add_separator()
        themes_menu.add_command(label="System",command= lambda : systemOT.changetheme("system",root))
        
    def loadVersion(self,root):
        self.add_command(label="version", command=lambda: alertBox.Alert(root,"version : v1.0.12","version").show())




    