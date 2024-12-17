import json

def changetheme(theme,root):
    try:
        with open("settings.json", "r") as file:
            settings = json.load(file)
        settings["themes"]["current"] = theme
        with open("settings.json", "w") as file:
            json.dump(settings, file)
    except Exception as e:
        pass
    
    root.loadTheme()