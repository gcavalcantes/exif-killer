try:
    # for Python3
    from tkinter import *
except ImportError:
    # for Python2
    from Tkinter import *


class Interface():
    # TODO Creates a screen for the main window
    def __init__(self, master=None):
        # Changes the window name
        master.title("Exif Killer")
        # Changes the dimensions of the window
        master.geometry('600x400+50+50')
        # Main frame of the app's window
        self.widget_main = Frame(master)
        self.widget_main.pack()

        # Menu bar
        self.menu_bar = Menu()
        self.menu_about = Menu(self.menu_bar, tearoff=False)
        self.menu_options = Menu(self.menu_bar, tearoff=False)

        self.menu_bar.add_cascade(label='Options', menu=self.menu_options)
        self.menu_bar.add_cascade(label='About', menu=self.menu_about)

        # Display of menu bar in the app
        master.config(menu=self.menu_bar)

        # Tool bar
        self.toolbar = Label(master)
        self.toolbar.pack(side=TOP, fill=X)

        # TODO Create the options menu items
        self.menu_options.add_command(
            label="Exit", command=self.widget_main.quit)

        # Message at the top of the screen
        self.message = Label(
            self.widget_main, text="Relevant messages are shown here")
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
