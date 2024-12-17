from tkinter import *
import json
from systemOT import *


class Navbar(Menu):
    def __init__(self,root):
        super().__init__()
        self.loadWidget(root)
        
        

    def loadWidget(self,root):
        self.folderWidget()
        self.themesWidget(root)
        
    def folderWidget(self):
        folder_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Folder", menu=folder_menu)
        folder_menu.add_command(label="Open", accelerator="Ctrl+O")
        folder_menu.add_command(label="Close", accelerator="Ctrl+C")
        

    def themesWidget(self,root):
        themes_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Themes", menu=themes_menu)
        themes_menu.add_command(label="Light",command= lambda : changetheme("light",root))
        themes_menu.add_command(label="Dark",command= lambda : changetheme("dark",root))
        # themes_menu.add_command(label="System",command= lambda : changetheme("system",root))
