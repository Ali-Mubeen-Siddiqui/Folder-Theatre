from customtkinter import *
import json
from . import alertBox

class StatusBar(CTkFrame):
    def __init__(self,root):
        super().__init__(master=root, height=20)
        self.res = self.display(root)
        

    def display(self,root):
        cpath = self.displayPath(root)
        return cpath

    def displayPath(self,root):
        try:
            with open("components/settings.json","r") as file:
                
                setting = json.load(file)
                if setting["path"]:
                    cpath = CTkLabel(self,text=f"  path | {setting["path"]}")
                else:
                    cpath = CTkLabel(self,text=f"  no folder opened")
        except Exception as e:
            alert = alertBox.Alert(root,"unable to fetch the path","error")
            cpath = CTkLabel(self,text=f"  error occurred while loading path")

            
            
        cpath.pack(side=LEFT)
        return cpath

    def refreshPath(self,path,cpath):
        cpath.configure(text=f"  path | {path}")
        
        
