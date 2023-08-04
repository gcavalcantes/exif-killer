from tkinter import *

class Interface():
    # TODO Creates a screen for the main window
    def __init__(self, master = None):
        self.wiget_main = Frame(master)
        self.wiget_main.pack()
        # Message at the top of the screen
        self.message = Label(self.wiget_main, text="Relevant messages are shown here")
        self.message["font"] = ("Verdana", "10", "italic", "bold")
        self.message.pack()
        # Exit button
        self.exit = Button(self.wiget_main)
        self.exit["text"] = "Exit"
        self.exit["font"] = ("Verdana", "10")
        self.exit["width"] = 5
        self.exit["command"] = self.wiget_main.quit
        self.exit.pack(side=RIGHT)

root = Tk()
Interface(root)
root.mainloop()