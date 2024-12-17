from customtkinter import *
import json

class StatusBar(CTkFrame):
    def __init__(self,root):
        super().__init__(master=root, height=20)
        self.res = self.display()
        

    def display(self):
        cpath = self.displayPath()
        return cpath

    def displayPath(self):
        with open("settings.json","r") as file:
            setting = json.load(file)
            if setting["path"]:
                cpath = CTkLabel(self,text=f"  path | {setting["path"]}")
            else:
                cpath = CTkLabel(self,text=f"  no folder opened")
                

            
            
        cpath.pack(side=LEFT)
        return cpath

    def refreshPath(self,path,cpath):
        cpath.configure(text=f"  path | {path}")
        
        
