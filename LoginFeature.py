import tkinter as tk
import tkinter.messagebox

class LoginInterface():
    def __init__(self):
        
        self.LoginWindow = tk.Tk()
        self.LoginWindow.title("Login")
        self.LoginWindow.geometry("300x341")
        self.LoginWindow.config(background = '#08D0FF')

        # Variable
        self.UserNameVar = tk.StringVar()
        self.PasswordVar = tk.StringVar()

        # Frame
        self.TitileFrame = tk.Frame(self.LoginWindow)
        self.TitileFrame.pack(side = 'top', pady = 10)
        self.TitileFrame.config(background = '#08D0FF')

        self.mainFrame = tk.Frame(self.LoginWindow)
        self.mainFrame.pack()
        self.mainFrame.config(background = '#08D0FF')

        self.buttonFrame = tk.Frame(self.LoginWindow)
        self.buttonFrame.pack()
        self.buttonFrame.config(background = '#08D0FF')

        # Interface
        self.lblTItle = tk.Label(self.TitileFrame, text = 'Book Mannger', bg = '#08D0FF', font = ('Times',30,))
        self.lblTItle.pack(fill = 'x')

        self.lblLoignSubtitle = tk.Label(self.TitileFrame, text = 'Login', bg = '#08D0FF', font = ('Times',20,))
        self.lblLoignSubtitle.pack()

        self.lblEmail_LoginIngterface = tk.Label(self.mainFrame, text = 'User Name :', bg = '#08D0FF', height = '3', font = ('defule',15,), anchor = 'w')
        self.lblEmail_LoginIngterface.grid(row = 0, column = 0)

        self.InputEmail_LoginInterface = tk.Entry(self.mainFrame, textvariable = self.UserNameVar)
        self.InputEmail_LoginInterface.grid(row = 0, column = 1)

        self.lblPassword_LoginInterface = tk.Label(self.mainFrame, text = 'Password :', bg = '#08D0FF', height = '3', font = ('defule',15,), anchor = 'w')
        self.lblPassword_LoginInterface.grid(row = 1, column = 0)

        self.InputPassword_LoginInterface = tk.Entry(self.mainFrame, show  = '*', textvariable = self.PasswordVar)
        self.InputPassword_LoginInterface.grid(row = 1, column = 1)

        self.btnLogin_LoginInterface = tk.Button(self.buttonFrame, text = 'Login', width = '10', command = self.Login_Function)
        self.btnLogin_LoginInterface.grid(row = 0, column = 0, pady = 20)

        self.btnSignup_LoginInterface = tk.Button(self.buttonFrame ,text = 'Sign up', width = '10')
        self.btnSignup_LoginInterface.grid(row = 0, column = 2, pady = 20)
 
        self.btnExit_LoginInterface = tk.Button(self.buttonFrame, text = 'Exit', width = '10', command = self.LoginWindow.destroy)
        self.btnExit_LoginInterface.grid(row = 1, column = 1, pady = 20)
          
        tk.mainloop()

    def Login_Function(self):

        User_Name = "Admin"
        Password = "Admin"

        if (self.UserNameVar.get() == User_Name) and (self.PasswordVar.get() == Password):
            tk.messagebox.showinfo('Login Succesfully' , 'Loadaing...')
            self.LoginWindow.destroy()
        else:
            tk.messagebox.showinfo('Login' , 'Login Fail Please enter correct User name & Password')
            print(self.UserNameVar.get())
            print(self.PasswordVar.get())
        


LoginInterface()