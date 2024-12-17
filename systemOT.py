import json
from alertBox import Alert

def changetheme(theme,root):
    try:
        with open("settings.json", "r") as file:
            settings = json.load(file)
        if theme == "system":
            # handle system theme mode, e.g., get the system theme and set it
            # for now, just set it to a default theme
            if root.cget("bg") == "SystemButtonFace":
                theme = "light"
            else:
                theme = "dark"
            
        settings["themes"]["current"] = theme
        with open("settings.json", "w") as file:
            json.dump(settings, file)
    except Exception as e:
        alrt = Alert(root,"unable to apply the theme")
        alrt.show()
       
    
    root.loadTheme()