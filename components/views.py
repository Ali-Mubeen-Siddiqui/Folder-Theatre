from customtkinter import *

class view(CTkTabview):
    def __init__(self,root,statusKey):
        self.root = root
        self.statusKey = statusKey
        super().__init__(master=root,fg_color="#D3D3D3",height=134,segmented_button_selected_color="grey10",border_width=0)  # A dark grey like shade of selected

        self.loadView()
        self.pack(fill=BOTH,expand=True,anchor=NW,pady=0,padx=0)
        

    def loadView(self):
        self.loadHome()
        self.loadSort()
        self.loadNotage()
        self.loadSearch()
        self.loadSettings()
        self.loadHelp()
        self.loadhistory()


    def loadHome(self):
        self.add("Home")
       
        
    def loadSort(self):
        self.add("Sort")

    def loadNotage(self):
        self.add("Notes")

    def loadSearch(self):
        self.add("Search")

    def loadSettings(self):
        self.add("Settings")

    def loadHelp(self):
        self.add("Help")

    def loadhistory(self):
        self.add("History")