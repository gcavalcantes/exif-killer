# This file deals with the "About" window

#import tkinter acourding to the Python version
try:
    # For Python 3
    from tkinter import *
except ImportError:
    # For Python 2
    from Tkinter import *

class AboutWindow():
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("About this program")
        self.geometry("200:200")