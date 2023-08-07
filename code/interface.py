from tkinter import *

class Interface():
    # TODO Creates a screen for the main window
    def __init__(self, master = None):
        self.widget_main = Frame(master)
        self.widget_main.pack()
        # Message at the top of the screen
        self.message = Label(self.widget_main, text="Relevant messages are shown here")
        self.message["font"] = ("Verdana", "10", "italic", "bold")
        self.message.pack()
        # Kill Exif button
        self.kill_exif = Button(self.widget_main)
        self.kill_exif["text"] = "Kill Exif"
        self.kill_exif["font"] = ("Verdana", "10")
        self.kill_exif["width"] = 5
        self.kill_exif.bind("<Button-1>", self.killExif)
        self.kill_exif.pack(side=LEFT)
        # Exit button
        self.exit = Button(self.widget_main)
        self.exit["text"] = "Exit"
        self.exit["font"] = ("Verdana", "10")
        self.exit["width"] = 5
        self.exit["command"] = self.widget_main.quit
        self.exit.pack(side=RIGHT)

    # TODO call the exif killer function
    def killExif(self, event):
        pass

root = Tk()
Interface(root)
root.mainloop()