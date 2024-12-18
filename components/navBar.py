from tkinter import *
import json
from . import systemOT
from . import openClose
from . import alertBox


class Navbar(Menu):
    def __init__(self,root,statusKey,arKey):
        super().__init__()
        self.statusKey = statusKey
        self.arKey = arKey
        self.loadWidget(root)
        
        

    def loadWidget(self,root):
        self.folderWidget(root)
        self.themesWidget(root)
        self.loadVersion(root)
        
    def folderWidget(self,root):
        folder_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Folder", menu=folder_menu)
        folder_menu.add_command(label="Open", accelerator="Ctrl+O", command = lambda : openClose.open_folder(root,self.statusKey))
        folder_menu.add_command(label="Close", accelerator="Ctrl+C",command = lambda : openClose.close_folder(root,self.statusKey))
        

    def themesWidget(self,root):
        themes_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Themes", menu=themes_menu)
        themes_menu.add_command(label="Light",command= lambda : systemOT.changetheme("light",root,self.arKey))
        themes_menu.add_command(label="Dark",command= lambda : systemOT.changetheme("dark",root,self.arKey))
        themes_menu.add_separator()
        themes_menu.add_command(label="System",command= lambda : systemOT.changetheme("system",root,self.arKey))
        
    def loadVersion(self,root):
        self.add_command(label="version", command=lambda: alertBox.Alert(root,"version : v1.0.12","version").show())




    