import tkinter as tk
import tkinter.messagebox
import tkinter.ttk

class SignupFeature():

    def __init__(self):
        self.sign_window = tk.Toplevel()
        self.sign_window.title("Sign Up")
        
        # Frame 
        self.TitleFrame = tk.Frame(self.sign_window)
        self.TitleFrame.pack(side = 'top', fill = 'x')

        self.mainFrame = tk.Frame(self.sign_window)
        self.mainFrame.pack()
        

SignupFeature()