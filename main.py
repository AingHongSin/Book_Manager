import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.filedialog



class MainfileApplication():

    def __init__(self):

        self.Main_Window = tk.Tk()
        self.Main_Window.title("Book Manager")
        self.Main_Window.geometry("1100x500+300+200")
        self.Main_Window.resizable(False, False)

        # Variable
        self.btn_All_AuthorName = ['Author1', 'Author2', 'Author3']
        self.Amount_Of_Button_Authorlist = []
        self.ListBook_for_each_Author = []

        # Frame
        self.topFrame_mainWindow = tk.Frame(self.Main_Window)
        self.topFrame_mainWindow.pack(side = 'top', fill = 'x')
        self.topFrame_mainWindow.config(background = '#666666')
        
        self.leftFrame_mainWindow = tk.Frame(self.Main_Window)
        self.leftFrame_mainWindow.pack(side = 'left', fill = 'y')
        self.leftFrame_mainWindow.config(background = '#a6a6a6')

        self.rightFrame_mainWindow = tk.Frame(self.Main_Window)
        self.rightFrame_mainWindow.pack(fill = 'both')
        
        # InterFace 
                            # TopFrame
        self.lblTitle_TopFrame = tk.Label(self.topFrame_mainWindow, text = 'Book Manager', font = ('defule',28,'bold'), bg = '#666666')
        self.lblTitle_TopFrame.pack()


                            # LeftFrame
        self.btnHome_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Home', height = '2', width = '15', command = self.homeInterfaceInterface)
        self.btnHome_leftFrame.pack()
        #self.btnHome_leftFrame.configure({"bg": "white", "activebackground": "white"})

        self.btnLibrary_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Library', height = '2', width = '15', command = self.libraryInterface)
        self.btnLibrary_leftFrame.pack()

        self.btnAuthor_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Author', height = '2', width = '15', command = self.AuthorInterface)
        self.btnAuthor_leftFrame.pack()
        
        self.btnCategory_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Category', height = '2', width = '15', command = self.CategoryInterface)
        self.btnCategory_leftFrame.pack()

        self.btnFavorit_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Fevorite', height = '2', width = '15', command = self.FavoritInterface)
        self.btnFavorit_leftFrame.pack()

        self.btnAlbum_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Album', height = '2', width = '15', command = self.AlbumInterface)
        self.btnAlbum_leftFrame.pack()

        self.btnExit_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Exit', height = '2', width = '15', command = self.Main_Window.destroy)
        self.btnExit_leftFrame.pack(side = 'bottom')

        self.homeInterfaceInterface()

        self.Main_Window.mainloop()

    def homeInterfaceInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_HomeInterface.pack()

        self.mainFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_HomeInterface.pack(pady = 40)

        # Interface
                        # Title
        self.lblTitle_HomeIterface = tk.Label(self.topFrame_HomeInterface, text = 'Welcome\nto\nBook Manager', font = ('Times',20,'bold'))
        self.lblTitle_HomeIterface.pack()

                        # Main
        self.btnLibrary_HomeInterface = tk.Button(self.mainFrame_HomeInterface, text = 'Library', width = '20', height = '4', command = self.libraryInterface)
        self.btnLibrary_HomeInterface.grid(row = 0, column = 0)

        self.btnAuthor_homeInterface = tk.Button(self.mainFrame_HomeInterface, text = 'Author', width = '20', height = '4', command = self.AuthorInterface)
        self.btnAuthor_homeInterface.grid(row = 0, column = 1)

        self.btnCategory_homeInterface = tk.Button(self.mainFrame_HomeInterface, text = 'Category', width = '20', height = '4', command = self.CategoryInterface)
        self.btnCategory_homeInterface.grid(row = 1, column = 0)

        self.btnFavorit_homeInterface = tk.Button(self.mainFrame_HomeInterface, text = 'Favorit', width = '20', height = '4', command = self.FavoritInterface)
        self.btnFavorit_homeInterface.grid(row = 1, column = 1)

        self.btnAlbum_homeInterfac = tk.Button(self.mainFrame_HomeInterface, text = 'Albun', width = '20', height = '4', command = self.AlbumInterface)
        self.btnAlbum_homeInterfac.grid(row = 2, column = 0, columnspan = 2)


    def libraryInterface(self):

        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_LibraryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_LibraryInterface.pack(side = 'top', fill = 'x')
        self.topFrame_LibraryInterface.config(background = '#c8c8c8')

        self.mainFrame_libraryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_libraryInterface.pack()
        
        # Interface
                            # Tapbar
        self.lblnameTap_libraryInterface = tk.Label(self.topFrame_LibraryInterface, text = 'Library', font = ('Times',20,'bold'), bg = '#c8c8c8')
        self.lblnameTap_libraryInterface.pack(side = 'right')

        self.btnAddBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Add', width = '10',height = '2')
        self.btnAddBook_LibraryInterface.pack(side = 'left')

        self.btnDeleteBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Delete', width = '10', height ='2')
        self.btnDeleteBook_LibraryInterface.pack(side = 'left')      


                            # main Interface
        self.listBook_libraryInterface = tk.ttk.Treeview(self.mainFrame_libraryInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_libraryInterface.pack(padx = '10', pady = '5')

        self.listBook_libraryInterface.column(1, width = '200')
        self.listBook_libraryInterface.heading(1, text = 'Title')

        self.listBook_libraryInterface.column(2, width = '200')
        self.listBook_libraryInterface.heading(2, text = 'Authot')

        self.listBook_libraryInterface.column(3, width = '150')
        self.listBook_libraryInterface.heading(3, text = 'Category')

        self.listBook_libraryInterface.column(4, width = '100')
        self.listBook_libraryInterface.heading(4, text = 'Last Readed')
        
        self.listBook_libraryInterface.column(5, width = '100')
        self.listBook_libraryInterface.heading(5, text = 'Date Added')
        
        self.listBook_libraryInterface.column(6, width = '80')
        self.listBook_libraryInterface.heading(6, text = 'Size')
        
        self.listBook_libraryInterface.column(7, width = '80')
        self.listBook_libraryInterface.heading(7, text = 'Favorite')

    def AuthorInterface(self):

        
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_AuthorInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AuthorInterface.config(background = '#dadada')

        self.leftFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_AuthorInterface.pack(side = 'left', fill = 'y')
        self.leftFrame_AuthorInterface.configure(background = '#c8c8c8')

        self.mainFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_AuthorInterface.pack(fill = 'both')

                # Interface
        self.lblnameTap_AuthorInterface = tk.Label(self.topFrame_AuthorInterface, text = 'Author', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_AuthorInterface.pack()

        self.lblNameTapAuthor = tk.Label(self.leftFrame_AuthorInterface, text = 'Author Name',width = '15')
        self.lblNameTapAuthor.pack()

        self.listBook_AuthorInterface = tk.ttk.Treeview(self.mainFrame_AuthorInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_AuthorInterface.pack(padx = '10', pady = '5')

        self.listBook_AuthorInterface.column(1, width = '150')
        self.listBook_AuthorInterface.heading(1, text = 'Title')

        self.listBook_AuthorInterface.column(2, width = '150')
        self.listBook_AuthorInterface.heading(2, text = 'Author')

        self.listBook_AuthorInterface.column(3, width = '150')
        self.listBook_AuthorInterface.heading(3, text = 'Category')

        self.listBook_AuthorInterface.column(4, width = '100')
        self.listBook_AuthorInterface.heading(4, text = 'Last Readed')
        
        self.listBook_AuthorInterface.column(5, width = '100')
        self.listBook_AuthorInterface.heading(5, text = 'Date Added')
        
        self.listBook_AuthorInterface.column(6, width = '80')
        self.listBook_AuthorInterface.heading(6, text = 'Size')
        
        self.listBook_AuthorInterface.column(7, width = '80')
        self.listBook_AuthorInterface.heading(7, text = 'Favorite')

        self.Backenf_of_AuthorInterface()
        print("work")

    ########################################################################################################################################################################
    def Backenf_of_AuthorInterface(self):
        for i in range(len(self.btn_All_AuthorName)):
            self.Amount_Of_Button_Authorlist.append(tk.Button(self.leftFrame_AuthorInterface, text = self.btn_All_AuthorName[i], width = '15', height = '2', command = lambda c=i: self.ListName_for_Each_Author(c)))
            self.Amount_Of_Button_Authorlist[i].pack()
    ########################################################################################################################################################################

    ########################################################################################################################################################################
    def ListName_for_Each_Author(self, c):

        for a in self.ListBook_for_each_Author:
            print('',end = '', sep='')
        self.listBook_AuthorInterface = tk.ttk.Treeview(self.mainFrame_AuthorInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_AuthorInterface.pack(padx = '10', pady = '5')

        self.listBook_AuthorInterface.column(1, width = '150')
        self.listBook_AuthorInterface.heading(1, text = 'Title')

        self.listBook_AuthorInterface.column(2, width = '150')
        self.listBook_AuthorInterface.heading(2, text = 'Author')

        self.listBook_AuthorInterface.column(3, width = '150')
        self.listBook_AuthorInterface.heading(3, text = 'Category')

        self.listBook_AuthorInterface.column(4, width = '100')
        self.listBook_AuthorInterface.heading(4, text = 'Last Readed')
        
        self.listBook_AuthorInterface.column(5, width = '100')
        self.listBook_AuthorInterface.heading(5, text = 'Date Added')
        
        self.listBook_AuthorInterface.column(6, width = '80')
        self.listBook_AuthorInterface.heading(6, text = 'Size')
        
        self.listBook_AuthorInterface.column(7, width = '80')
        self.listBook_AuthorInterface.heading(7, text = 'Favorite')

    ########################################################################################################################################################################

    def CategoryInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()
        # Frame
        self.topFrame_CategoryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_CategoryInterface.pack(side = 'top', fill = 'x')
        self.topFrame_CategoryInterface.config(background = '#dadada')

        self.leftFrame_CategoryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_CategoryInterface.pack(side = 'left', fill = 'y')

        self.mainFrame_CategoryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_CategoryInterface.pack()


        # Interface
        self.lblnameTap_CategoryInterface = tk.Label(self.topFrame_CategoryInterface, text = 'Category', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_CategoryInterface.pack()



        self.listBook_CategoryInterface = tk.ttk.Treeview(self.mainFrame_CategoryInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_CategoryInterface.pack(padx = '10', pady = '5')

        self.listBook_CategoryInterface.column(1, width = '200')
        self.listBook_CategoryInterface.heading(1, text = 'Title')

        self.listBook_CategoryInterface.column(2, width = '200')
        self.listBook_CategoryInterface.heading(2, text = 'Authot')

        self.listBook_CategoryInterface.column(3, width = '150')
        self.listBook_CategoryInterface.heading(3, text = 'Category')

        self.listBook_CategoryInterface.column(4, width = '100')
        self.listBook_CategoryInterface.heading(4, text = 'Last Readed')
        
        self.listBook_CategoryInterface.column(5, width = '100')
        self.listBook_CategoryInterface.heading(5, text = 'Date Added')
        
        self.listBook_CategoryInterface.column(6, width = '80')
        self.listBook_CategoryInterface.heading(6, text = 'Size')
        
        self.listBook_CategoryInterface.column(7, width = '80')
        self.listBook_CategoryInterface.heading(7, text = 'Favorite')


    def FavoritInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()
        # Frame
        self.topFrame_FavoriteInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_FavoriteInterface.pack(side = 'top', fill = 'x')
        self.topFrame_FavoriteInterface.config(background = '#dadada')
        
        self.mainFrame_FevoriteInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_FevoriteInterface.pack(fill = 'both')
        
        # Interface
                            # Tapbar
        self.lblnameTap_FavoriteInterface = tk.Label(self.topFrame_FavoriteInterface, text = 'Favorite', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_FavoriteInterface.pack(side = 'right')

        self.btnAddBook_FavoriteInterface = tk.Button(self.topFrame_FavoriteInterface, text = 'Add', width = '10',height = '2')
        self.btnAddBook_FavoriteInterface.pack(side = 'left')

        self.btnDeleteBook_FavoriteInterface = tk.Button(self.topFrame_FavoriteInterface, text = 'Delete', width = '10', height ='2')
        self.btnDeleteBook_FavoriteInterface.pack(side = 'left')      


                            # main Interface
        self.listBook_FavoriteInterface = tk.ttk.Treeview(self.mainFrame_FevoriteInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_FavoriteInterface.pack(padx = '10', pady = '5')

        self.listBook_FavoriteInterface.column(1, width = '150')
        self.listBook_FavoriteInterface.heading(1, text = 'Title')

        self.listBook_FavoriteInterface.column(2, width = '150')
        self.listBook_FavoriteInterface.heading(2, text = 'Authot')

        self.listBook_FavoriteInterface.column(3, width = '150')
        self.listBook_FavoriteInterface.heading(3, text = 'Category')

        self.listBook_FavoriteInterface.column(4, width = '100')
        self.listBook_FavoriteInterface.heading(4, text = 'Last Readed')
        
        self.listBook_FavoriteInterface.column(5, width = '100')
        self.listBook_FavoriteInterface.heading(5, text = 'Date Added')
        
        self.listBook_FavoriteInterface.column(6, width = '80')
        self.listBook_FavoriteInterface.heading(6, text = 'Size')
        
        self.listBook_FavoriteInterface.column(7, width = '80')
        self.listBook_FavoriteInterface.heading(7, text = 'Favorite')
        
    def AlbumInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_AlbumInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AlbumInterface.config(background = '#dadada')

        self.leftFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_AlbumInterface.pack(side = 'left', fill = 'y')

        # Interface
        self.lblnameTap_AlbumInterface = tk.Label(self.topFrame_AlbumInterface, text = 'Album', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_AlbumInterface.pack()


if __name__ == "__main__":
    MainfileApplication() 
