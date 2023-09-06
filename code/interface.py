try:
    # for Python3
    from tkinter import *
    from tkinter import filedialog
except ImportError:
    # for Python2
    from Tkinter import *

from exif_killer import exifKiller


class Interface():
    # Creates a screen for the main window
    def __init__(self, master=None, text_variable=None):
        # Changes the window name
        master.title("Exif Killer")
        # Changes the dimensions of the window
        master.geometry('450x125+50+50')
        # Main frame of the app's window
        self.widget_main = Frame(master)
        self.widget_main.pack()

        # Status of the exif killing process.
        self.STATUS = ["Exif content has successfuly been deleted",
                       "No exif content has been detected", "Falha ao carregar arquivo", "", ""]

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

        # Create the options menu items
        self.menu_options.add_separator()
        self.menu_options.add_command(
            label="Exit", command=self.widget_main.quit)

        # Option that opens the about window
        self.menu_about.add_command(
            label="About this program", command=lambda: self.aboutWindow(master)
        )

        # Labe for the image path
        self.user_input_label = Label(
            self.widget_main, text="Select the image: ")
        self.user_input_label.grid(row=0, column=0, sticky=NW)

        # Get the user input
        self.input = StringVar(master)
        # Input for the image path
        self.user_input = Entry(self.widget_main, textvariable=input, width=50)
        self.user_input.grid(row=1, column=0, sticky=NW)

        # Message at the top of the screen
        self.message = Label(
            self.widget_main, text="Status: Waiting for command")
        self.message["font"] = ("Verdana", "10", "italic", "bold")
        self.message.grid(row=2, column=0, sticky=NW)

        # Select image button
        self.select_file_button = Button(
            self.widget_main, command=self.browseFiles)
        self.select_file_button["text"] = "Select File"
        self.select_file_button["font"] = ("Verdana", "10")
        self.select_file_button["width"] = 9
        self.select_file_button.bind("<Button-1>")
        self.select_file_button.grid(row=1, column=1, sticky=NE, padx=4)

        # Kill Exif button
        self.kill_exif = Button(
            self.widget_main, command=lambda:  self.killExif(self.user_input.get()))
        self.kill_exif["text"] = "Kill Exif"
        self.kill_exif["font"] = ("Verdana", "10")
        self.kill_exif["width"] = 6
        self.kill_exif.bind("<Button-1>")
        self.kill_exif.grid(row=3, column=0, sticky=W)

        # Exit button
        self.exit = Button(self.widget_main)
        self.exit["text"] = "Exit"
        self.exit["font"] = ("Verdana", "10")
        self.exit["width"] = 5
        self.exit["command"] = self.widget_main.quit
        self.exit.grid(row=3, column=1, sticky=E)

    # Call the exif killer function
    def killExif(self, path):
        if (path != '' or path != None):
            try:
                exifKiller(path)

            except AttributeError as atrib_error:
                print(atrib_error)
            else:
                self.message["text"] = self.STATUS[2]

    # About window
    def aboutWindow(self, window):
        credits_message = "Code and interface: Gabriel Cavalcante"
        about = Toplevel(window)
        about.title("About this program")
        about.geometry("250x200")
        version_label = Label(about, text="Exif Killer version: 0.0.1")
        version_label.grid()
        credits_label = Label(about, text=credits_message)
        credits_label.grid()

    # Browse files
    def browseFiles(self):
        accepted_images = [".png", '.jpg', ".jfif", ".jpeg", ".bmp"]
        filename = filedialog.askopenfile(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Image files",
                                                      accepted_images),
                                                     ("all files",
                                                      "*.*")))
        # Change the text in the input
        self.user_input.insert(0, filename.name)


if __name__ == "__main__":
    # Runs the app.
    root = Tk()
    Interface(root)
    root.mainloop()
