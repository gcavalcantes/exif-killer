# This file deals with the "About" window

# import tkinter acourding to the Python version
try:
    # For Python 3
    from tkinter import *
except ImportError:
    # For Python 2
    from Tkinter import *


class AboutWindow():
    def aboutWindow(window):
        about = Toplevel(window)
        about.title("About this program")
        about.geometry("200x200")
        version_label = Label(about, text="Exif Killer version: 0.0.1")
        version_label.pack()
