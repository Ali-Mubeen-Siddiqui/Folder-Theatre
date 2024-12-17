import json
from tkinter import filedialog
import os

def open_folder(root,statusKey):
    path = filedialog.askdirectory()
    if path:
        with open("settings.json", "r") as file:
            settings = json.load(file)
        settings["path"] = path
        with open("settings.json", "w") as file:
            json.dump(settings, file)

        statusKey.refreshPath(path,statusKey.res)

        
        


