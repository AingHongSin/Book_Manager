import tkinter as tk
import tkinter.messagebox
import tkinter.ttk

class SignupFeature():

    def __init__(self):
        self.sign_window = tk.Tk()
        self.sign_window.title("Sign Up")
        
        # Frame 
        self.TitleFrame = tk.Frame(self.sign_window)
        self.TitleFrame.pack(side = 'top', fill = 'x')

        self.mainFrame = tk.Frame(self.sign_window)
        self.mainFrame.pack()

        # mian
        self.TitleInterface = tk.Label(self.TitleFrame, text = 'Sign up', font = ('defule',28,'bold'))
        self.TitleInterface.pack()

        self.lblName_signin = tk.Label(self.mainFrame, text = 'Name:')
        self.lblName_signin.grid(row = 0, column = 0)

        self.inpName_signin = tk.Entry(self.mainFrame)
        self.inpName_signin.grid(row = 0, column = 1)

        self.lbl
        
        self.sign_window.mainloop()

SignupFeature()