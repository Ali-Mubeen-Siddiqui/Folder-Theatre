import json
from tkinter import filedialog
import os

def open_folder(root,statusKey):
    path = filedialog.askdirectory()
    if path:
        try:
            with open("components/settings.json", "r") as file:
                settings = json.load(file)
            settings["path"] = path
            with open("components/settings.json", "w") as file:
                json.dump(settings, file)
            statusKey.refreshPath(path,statusKey.res)
        except Exception as e:
            statusKey.refreshPath(" unable to load the path", statusKey.res)
        
        


