import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import os
from PIL import ImageTk, Image
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from collections import OrderedDict
import datetime
import sqlite3
import shutil



class MainfileApplication():

    def __init__(self):
                
        self.Main_Window = tk.Tk()
        self.Main_Window.title("My_BooK")
        self.Main_Window.geometry("1500x700+100+100")
        #self.Main_Window.resizable(False, False)
        
        self.Amount_Book = 0
        self.datalist_of_Database = []
        self.Add_Data_Into_Database()




        # Variable
                # Author Tuple
        self.btn_All_AuthorName = ['Author1', 'Author2', 'Author3']
        self.Author_index = 0

                # Category Tuple
        self.btn_All_CategoryName = ['Category1', 'Category2', 'Category3']
        self.Category_index = 0

                # Album Tuple
        # Frame

        self.leftFrame_mainWindow = tk.Frame(self.Main_Window)
        self.leftFrame_mainWindow.pack(side = 'left', fill = 'y')
        self.leftFrame_mainWindow.config(background = '#eaeaea')

        #self.topFrame_mainWindow = tk.Frame(self.Main_Window )
        #self.topFrame_mainWindow.pack(side = 'top', fill = 'x')
        #self.topFrame_mainWindow.config(background = '#666666')
        
        self.rightFrame_mainWindow = tk.Frame(self.Main_Window)
        self.rightFrame_mainWindow.pack(fill = 'both')

            #
        self.LibraryPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Library2.png")
        self.LibraryPotho_image = self.LibraryPhoto.subsample(3,3)

        self.AuthorPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Author1.png")
        self.AuthorPotho_image = self.AuthorPhoto.subsample(3,3)

        self.CategoriesPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Categories.png")
        self.CategoriesPotho_image = self.CategoriesPhoto.subsample(3,3)

        self.FavoritPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Favorit.png")
        self.FavoritPhoto_image = self.FavoritPhoto.subsample(3,3)

        self.AlbumPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Album.png")
        self.AlbumPotho_image = self.AlbumPhoto.subsample(3,3)


        # InterFace 
                            # TopFrame
        #self.lblTitle_TopFrame = tk.Label(self.topFrame_mainWindow, text = 'My BooK', height = '2', font = ('defule',36,'bold'), bg = '#666666')
        #self.lblTitle_TopFrame.pack()


                            # LeftFrame
        self.btnRefresh_leftFrame = tk.Button(self.leftFrame_mainWindow, text = 'Refrash', width = '29', height = '2', command = self.resetApplication)
        self.btnRefresh_leftFrame.pack(side = 'top')

        self.homephoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/home.png")
        self.homePhoto_image = self.homephoto.subsample(1,1)

        self.btnHome_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.homePhoto_image, width = '260' , command = self.homeInterfaceInterface)
        self.btnHome_leftFrame.pack()
        #self.btnHome_leftFrame.configure({"bg": "white", "activebackground": "white"})


        self.btnLibrary_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.LibraryPotho_image, text = '\tLibrary \t\t', bg = 'red', compound = 'left',  command = self.libraryInterface)
        self.btnLibrary_leftFrame.pack()

        self.btnAuthor_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.AuthorPotho_image, text = '\tAuthor \t\t', compound = 'left', command = self.AuthorInterface)
        self.btnAuthor_leftFrame.pack()
        
        self.btnCategory_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.CategoriesPotho_image, text = '\tCategory \t\t', compound = 'left', command = self.CategoryInterface)
        self.btnCategory_leftFrame.pack()

        self.btnFavorit_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.FavoritPhoto_image, text = '\tFevorite \t\t',  compound = 'left', command = self.FavoritInterface)
        self.btnFavorit_leftFrame.pack()

        self.btnAlbum_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.AlbumPotho_image, text = '\tAlbum \t\t',  compound = 'left', command = self.AlbumInterface)
        self.btnAlbum_leftFrame.pack()

        self.btnExit_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '❌\tExit', height = '2', width = '29', command = self.Main_Window.destroy)
        self.btnExit_leftFrame.pack(side = 'bottom')

        self.homeInterfaceInterface()

        self.Main_Window.mainloop()
        
    def homeInterfaceInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_HomeInterface.pack( fill = 'x')
        self.topFrame_HomeInterface.config(background = '#eaeaea')


        self.mainFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_HomeInterface.pack()
    
        self.recentFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.recentFrame_HomeInterface.pack(side = 'bottom', fill = 'both')

        # Interface
                        # Title
        self.lblTitle_HomeIterface = tk.Label(self.topFrame_HomeInterface, text = 'Welcome\nto\nLibrary Owner', font = ('Times',20,'bold'), bg = '#eaeaea')
        self.lblTitle_HomeIterface.pack(pady = '5', fill = 'x', )

                        # Main
        self.LibraryPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Library2.png")
        self.LibraryPotho_image_HomeInterface = self.LibraryPhoto_HomeInterface.subsample(1,1)
        self.btnLibrary_HomeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.LibraryPotho_image_HomeInterface, text = '\t\tLibrary\t\t', compound = 'top', width = 300, font = ('default',15), command = self.libraryInterface)
        self.btnLibrary_HomeInterface.grid(row = 0, column = 0)

        self.AuthorPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Author1.png")
        self.AuthorPotho_image_HomeInterface = self.AuthorPhoto_HomeInterface.subsample(1,1)
        self.btnAuthor_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.AuthorPotho_image_HomeInterface, text = '\t\tAuthor\t\t\t\t', compound = 'top', font = ('default',15), command = self.AuthorInterface)
        self.btnAuthor_homeInterface.grid(row = 1, column = 0, columnspan = 2)

        self.CategoriesPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Categories.png")
        self.CategoriesPotho_image_HomeInterface = self.CategoriesPhoto_HomeInterface.subsample(1,1)
        self.btnCategory_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.CategoriesPotho_image_HomeInterface, text = '\t\tCategoriest\t\t', compound = 'top', font = ('default',15), command = self.CategoryInterface)
        self.btnCategory_homeInterface.grid(row = 0, column = 1)

        self.FavoritPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Favorit.png")
        self.FavoritPhoto_image_HomeInterface = self.FavoritPhoto_HomeInterface.subsample(1,1)
        self.btnFavorit_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.FavoritPhoto_image_HomeInterface, text = '\t\t\tFavorite\t\t', compound = 'top', font = ('default',15), command = self.FavoritInterface)
        self.btnFavorit_homeInterface.grid(row = 1, column = 1, columnspan = 2)

        self.AlbumPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Album.png")
        self.AlbumPotho_image_HomeInterface = self.AlbumPhoto_HomeInterface.subsample(1,1)
        self.btnAlbum_homeInterfac = tk.Button(self.mainFrame_HomeInterface, image = self.AlbumPotho_image_HomeInterface, text = '\t\tAlbum\t\t', compound = 'top', font = ('default',15), command = self.AlbumInterface)
        self.btnAlbum_homeInterfac.grid(row = 0, column = 2)

        self.RecentList_HomgInterface()

    def RecentList_HomgInterface(self):

        self.lblFrame = tk.LabelFrame(self.rightFrame_mainWindow, text = 'Recent')
        self.lblFrame.pack(fill = 'both', padx = '20', pady = '10')

        self.btnClearListRecentBook_HomeInterface = tk.Button(self.lblFrame, text = 'Clear Menu', width = '10', command = self.ClearRecentListBook_in_Database)
        self.btnClearListRecentBook_HomeInterface.pack(anchor = 'ne')

        self.listRecentBook_HomeInterface = tk.ttk.Treeview(self.lblFrame, column = ('ID', 'Title', 'Author', 'Lenght', 'Category', 'Last Readed', 'Date Added'), show = 'headings', height = '14')
        self.listRecentBook_HomeInterface.pack(pady = '10', padx = '10')

        self.listRecentBook_HomeInterface.column('ID', width = '50')
        self.listRecentBook_HomeInterface.heading('ID', text = 'ID')

        self.listRecentBook_HomeInterface.column('Title', width = '300')
        self.listRecentBook_HomeInterface.heading('Title', text = 'Title')

        self.listRecentBook_HomeInterface.column('Author', width = '250')
        self.listRecentBook_HomeInterface.heading('Author', text = 'Author')
        
        self.listRecentBook_HomeInterface.column('Lenght', width = '96')
        self.listRecentBook_HomeInterface.heading('Lenght', text = 'Length')

        self.listRecentBook_HomeInterface.column('Category', width = '150')
        self.listRecentBook_HomeInterface.heading('Category', text = 'Category')

        self.listRecentBook_HomeInterface.column('Last Readed', width = '160')
        self.listRecentBook_HomeInterface.heading('Last Readed', text = 'Last Readed')

        self.listRecentBook_HomeInterface.column('Date Added', width = '160')
        self.listRecentBook_HomeInterface.heading('Date Added', text = 'Date Added')

        self.Recent_Adding_to_list()

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

        self.btnAddBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Add', width = '10',height = '2', command = self.openFileDailog_for_AddFile)
        self.btnAddBook_LibraryInterface.pack(side = 'left')

        self.btnDeleteBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Delete', width = '10', height ='2')
        self.btnDeleteBook_LibraryInterface.pack(side = 'left')      

        self.btnDeleteBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Edit', width = '10', height ='2')
        self.btnDeleteBook_LibraryInterface.pack(side = 'left')   

        self.btnBookDetail_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Detail', width = '10', height = '2')
        self.btnBookDetail_LibraryInterface.pack(side = 'left')   

        self.btnFavoritAdding_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Favorit Adding', width = '15', height = '2', command = self.FavoritAddingBackend)
        self.btnFavoritAdding_LibraryInterface.pack(side = 'left')

                            # main Interface
        self.listBook_libraryInterface = tk.ttk.Treeview(self.mainFrame_libraryInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Category', 'Last Readed', 'Date Added'), show = 'headings', height = '40')
        self.listBook_libraryInterface.pack(padx = '10', pady = '10')

        self.listBook_libraryInterface.column('ID', width = '50')
        self.listBook_libraryInterface.heading('ID', text = 'ID')

        self.listBook_libraryInterface.column('Title', width = '300')
        self.listBook_libraryInterface.heading('Title', text = 'Title')

        self.listBook_libraryInterface.column('Author', width = '220')
        self.listBook_libraryInterface.heading('Author', text = 'Author')

        self.listBook_libraryInterface.column('Lenght', width = '140')
        self.listBook_libraryInterface.heading('Lenght', text = 'Length')

        self.listBook_libraryInterface.column('Category', width = '180')
        self.listBook_libraryInterface.heading('Category', text = 'Category')
    
        self.listBook_libraryInterface.column('Last Readed', width = '160')
        self.listBook_libraryInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_libraryInterface.column('Date Added', width = '160')
        self.listBook_libraryInterface.heading('Date Added', text = 'Date Added')

        #self.listBook_libraryInterface.column('Favorite', width = '80')
        #self.listBook_libraryInterface.heading('Favorite', text = 'Favorite')

        self.library_Data_Adding()


    def AuthorInterface(self):

        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_AuthorInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AuthorInterface.config(background = '#dadada')

        self.leftFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_AuthorInterface.pack(side = 'left', fill = 'y')
        #self.leftFrame_AuthorInterface.configure(background = '#c8c8c8')

        self.mainFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_AuthorInterface.pack(fill = 'both')

                # Interface

        self.btnAddBook_CategoryInterface = tk.Button(self.topFrame_AuthorInterface, text = 'Add Author', width = '10',height = '2')
        self.btnAddBook_CategoryInterface.pack(side = 'left')

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_AuthorInterface, text = 'Delete Author', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_AuthorInterface, text = 'Edit Author', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.lblnameTap_AuthorInterface = tk.Label(self.topFrame_AuthorInterface, text = 'Author', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_AuthorInterface.pack(side = 'right')

        self.AuthorNameList_AutorInterface()

        self.listBook_AuthorInterface = tk.ttk.Treeview(self.mainFrame_AuthorInterface, column = ('ID', 'Title', 'Author', 'Length', 'Category', 'Last_Readed' , 'Date_Added'), show = 'headings', height = '40')
        self.listBook_AuthorInterface.pack(padx = '10', pady = '10')

        self.listBook_AuthorInterface.column('ID', width = '50')
        self.listBook_AuthorInterface.heading('ID', text = 'ID')

        self.listBook_AuthorInterface.column('Title', width = '250')
        self.listBook_AuthorInterface.heading('Title', text = 'Title')

        self.listBook_AuthorInterface.column('Author', width = '200')
        self.listBook_AuthorInterface.heading('Author', text = 'Author')

        self.listBook_AuthorInterface.column('Length', width = '100')
        self.listBook_AuthorInterface.heading('Length', text = 'Length')

        self.listBook_AuthorInterface.column('Category', width = '130')
        self.listBook_AuthorInterface.heading('Category', text = 'Category')

        self.listBook_AuthorInterface.column('Last_Readed', width = '140')
        self.listBook_AuthorInterface.heading('Last_Readed', text = 'Last Readed')
        
        self.listBook_AuthorInterface.column('Date_Added', width = '140')
        self.listBook_AuthorInterface.heading('Date_Added', text = 'Date Added')
        
        #self.listBook_AuthorInterface.column(7, width = '100')
        #self.listBook_AuthorInterface.heading(7, text = 'Favorite')


    def AuthorNameList_AutorInterface(self):

        self.tvListName = tk.ttk.Treeview(self.leftFrame_AuthorInterface, column = ('Author_Name'), show = 'headings', height = '40')
        self.tvListName.pack(pady = '10')

        self.tvListName.column('Author_Name', width = '200')
        self.tvListName.heading('Author_Name', text = 'All Authors')

    def OnDoubleClick_Author(self, event):

        item = self.tvListName.selection()
        print("This is ", str(self.tvListName.item(item ,"values")[0]))
        
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
        self.btnAddBook_CategoryInterface = tk.Button(self.topFrame_CategoryInterface, text = 'Add Album', width = '10',height = '2')
        self.btnAddBook_CategoryInterface.pack(side = 'left')

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_CategoryInterface, text = 'Delete Album', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_CategoryInterface, text = 'Edit Album', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.lblnameTap_CategoryInterface = tk.Label(self.topFrame_CategoryInterface, text = 'Category', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_CategoryInterface.pack(side = 'right')

        self.AllCategoryList_CategoryInterface()

        self.listBook_CategoryInterface = tk.ttk.Treeview(self.mainFrame_CategoryInterface, column = ('ID', 'Title', 'Author', 'Length', 'Category', 'Last_Readed' , 'Date_Added'), show = 'headings', height = '40')
        self.listBook_CategoryInterface.pack(padx = '10', pady = '10')

        self.listBook_CategoryInterface.column('ID', width = '50')
        self.listBook_CategoryInterface.heading('ID', text = 'ID')

        self.listBook_CategoryInterface.column('Title', width = '250')
        self.listBook_CategoryInterface.heading('Title', text = 'Title')

        self.listBook_CategoryInterface.column('Author', width = '180')
        self.listBook_CategoryInterface.heading('Author', text = 'Author')

        self.listBook_CategoryInterface.column('Length', width = '98')
        self.listBook_CategoryInterface.heading('Length', text = 'Length')

        self.listBook_CategoryInterface.column('Category', width = '130')
        self.listBook_CategoryInterface.heading('Category', text = 'Category')
        
        self.listBook_CategoryInterface.column('Last_Readed', width = '160')
        self.listBook_CategoryInterface.heading('Last_Readed', text = 'Last Readed')

        self.listBook_CategoryInterface.column('Date_Added', width = '160')
        self.listBook_CategoryInterface.heading('Date_Added', text = 'Date Added')

    def AllCategoryList_CategoryInterface(self):

        self.tvListCategory = tk.ttk.Treeview(self.leftFrame_CategoryInterface, column = ('Category_Name'), show = 'headings', height = '40')
        self.tvListCategory.pack(pady = '10')

        self.tvListCategory.column('Category_Name', width = '200')
        self.tvListCategory.heading('Category_Name', text = 'All Categories')

        for Data in self.btn_All_CategoryName:
            self.tvListCategory.insert("", tk.END, self.Category_index, values = Data)
            self.Category_index = self.Category_index + 1
        self.tvListCategory.bind("<Double-1>", self.OnDoubleClick_Category)

    def OnDoubleClick_Category(self, event):

        item = self.tvListCategory.selection()
        print("This is ", str(self.tvListCategory.item(item ,"values")[0]))

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

        self.btnDeleteBook_FavoriteInterface = tk.Button(self.topFrame_FavoriteInterface, text = 'Delete', width = '10', height ='2', command = self.DeleteData_From_FavoriteList)
        self.btnDeleteBook_FavoriteInterface.pack(side = 'left')      

                            # main Interface
        self.listBook_FavoriteInterface = tk.ttk.Treeview(self.mainFrame_FevoriteInterface, column = ('ID', 'Title', 'Author', 'Length', 'Category', 'Last Readed', 'Date Added'), show = 'headings', height = '40')
        self.listBook_FavoriteInterface.pack(padx = '10', pady = '10')

        self.listBook_FavoriteInterface.column('ID', width = '50')
        self.listBook_FavoriteInterface.heading('ID', text = 'ID')

        self.listBook_FavoriteInterface.column('Title', width = '300')
        self.listBook_FavoriteInterface.heading('Title', text = 'Title')

        self.listBook_FavoriteInterface.column('Author', width = '220')
        self.listBook_FavoriteInterface.heading('Author', text = 'Author')

        self.listBook_FavoriteInterface.column('Length', width = '130')
        self.listBook_FavoriteInterface.heading('Length', text = 'Length')

        self.listBook_FavoriteInterface.column('Category', width = '200')
        self.listBook_FavoriteInterface.heading('Category', text = 'Category')

        self.listBook_FavoriteInterface.column('Last Readed', width = '160')
        self.listBook_FavoriteInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_FavoriteInterface.column('Date Added', width = '160')
        self.listBook_FavoriteInterface.heading('Date Added', text = 'Date Added')

        self.Favorite_Insrerting_Data_to_List()

    def AlbumInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_AlbumInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AlbumInterface.config(background = '#dadada')

        self.leftFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_AlbumInterface.pack(side = 'left', fill = 'y')

        self.mainFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_AlbumInterface.pack(fill = 'both')

        # Interface
        self.btnAddBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Add Album', width = '10',height = '2', command = self.addAlbum_Action)
        self.btnAddBook_AlbumInterface.pack(side = 'left')

        self.btnDeleteBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Delete Album', width = '10', height ='2')
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.btnDeleteBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Edit Album', width = '10', height ='2')
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.lblnameTap_AlbumInterface = tk.Label(self.topFrame_AlbumInterface, text = 'Album', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_AlbumInterface.pack(side = 'right')

        self.AlbumList_AlbumInterface()

        self.listBook_AlbumInterface = tk.ttk.Treeview(self.mainFrame_AlbumInterface, column = ('ID', 'Title', 'Author', 'Length', 'Category', 'Last_Readed', 'Date_Added'), show = 'headings', height = '40')
        self.listBook_AlbumInterface.pack(padx = '10', pady = '10')

        self.listBook_AlbumInterface.column('ID', width = '50')
        self.listBook_AlbumInterface.heading('ID', text = 'ID')

        self.listBook_AlbumInterface.column('Title', width = '250')
        self.listBook_AlbumInterface.heading('Title', text = 'Title')

        self.listBook_AlbumInterface.column('Author', width = '200')
        self.listBook_AlbumInterface.heading('Author', text = 'Author')

        self.listBook_AlbumInterface.column('Length', width = '100')
        self.listBook_AlbumInterface.heading('Length', text = 'Length')

        self.listBook_AlbumInterface.column('Category', width = '130')
        self.listBook_AlbumInterface.heading('Category', text = 'Category')

        self.listBook_AlbumInterface.column('Last_Readed', width = '140')
        self.listBook_AlbumInterface.heading('Last_Readed', text = 'Last Readed')
        
        self.listBook_AlbumInterface.column('Date_Added', width = '140')
        self.listBook_AlbumInterface.heading('Date_Added', text = 'Date Added')
        
    
    def AlbumList_AlbumInterface(self):
        self.listAllAlbum_AuthorInterface = tk.ttk.Treeview(self.leftFrame_AlbumInterface, show = 'headings', column = ('All_Album'), height = '40')
        self.listAllAlbum_AuthorInterface.pack(pady = '10')

        self.listAllAlbum_AuthorInterface.column('All_Album', width = '200')
        self.listAllAlbum_AuthorInterface.heading('All_Album', text = 'All Album')

    def addAlbum_Action(self):
        self.addAlbum_Interface = tk.Toplevel(self.Main_Window)
        self.addAlbum_Interface.title("Album Adding")

        self.mainFrame_AlbumAdding_topLevel = tk.Frame(self.addAlbum_Interface)
        self.mainFrame_AlbumAdding_topLevel.pack()

        self.buttonFrame_AlbumAdding_topLevel = tk.Frame(self.addAlbum_Interface)
        self.buttonFrame_AlbumAdding_topLevel.pack()

        self.lblNameAlbum = tk.Label(self.mainFrame_AlbumAdding_topLevel, text = 'Name')
        self.lblNameAlbum.grid(row = 0, column = 0)

        self.inputNameAlbum = tk.Entry(self.mainFrame_AlbumAdding_topLevel, width = '20')
        self.inputNameAlbum.grid(row = 0, column = 1)

        self.btnCancel = tk.Button(self.buttonFrame_AlbumAdding_topLevel, text = 'Cancel', width = '10', command = self.addAlbum_Interface.destroy)
        self.btnCancel.grid(row = 0, column = 0)

        self.btnDone = tk.Button(self.buttonFrame_AlbumAdding_topLevel, text = 'Done', width = '10', command = print("Done!..."))
        self.btnDone.grid(row = 0, column = 1)

        self.addAlbum_Interface.mainloop()
#___________________________________________________________________________________________BACK-END__________________________________________________________________#

    def Add_Data_Into_Database(self):

        # Database
        os.chdir('/Users/macbook/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        os.chdir('/Users/macbook/Documents/Project/Book_Manager/Data')

        self.d = os.listdir()

        self.c.execute("SELECT * FROM Data_list ")

        self.items = self.c.fetchall()

        for item in self.items:
            self.datalist_of_Database.append(item[1])

        self.Amount_Book = len(self.items) + 1

        for row in self.d:
            if row != '.DS_Store':
                print(row[0])
                if row in self.datalist_of_Database:
                    print("", end="")
                else:
                    pdf_path = str(row)
                    with open(pdf_path, 'rb') as f:
                        self.pdf = PdfFileReader(f)
                        self.information = self.pdf.getDocumentInfo()
                        self.number_of_pages = self.pdf.getNumPages()

                    ID = self.Amount_Book 
                    Title = str(row)
                    Author = (self.information.author)
                    Category = ('Unknown')
                    Number_of_Pages = (self.number_of_pages)
                    Last_Read = ('Unknown How')
                    Add_Date = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d,  %H:%M:%S"))

                    libraryData = [
                                (ID, Title, Author, Number_of_Pages, Category, Last_Read, Add_Date)
                                ]

                    self.c.executemany("INSERT INTO Data_list VALUES (?,?,?,?,?,?,?)" , libraryData)
                    self.conn.commit()
                    self.Amount_Book += 1
                               
    def library_Data_Adding(self):
        self.c.execute("SELECT * FROM Data_list ")

        self.items = self.c.fetchall()

        for item in self.items:
            if item[2] == None:
                self.listBook_libraryInterface.insert("", tk.END, values = (item[0], item[1], 'Unknown Author', item[3],  item[4], item[5], item[6] ))
            else: 
                self.listBook_libraryInterface.insert("", tk.END, values = (item[0], item[1], item[2], item[3],  item[4], item[5], item[6] ))
            self.listBook_libraryInterface.bind("<Double-Button-1>", self.openFeature)


    def openFeature(self, event):
        self.time_Now = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d,  %H:%M:%S"))
        item = self.listBook_libraryInterface.selection()
        ID_Data = str(self.listBook_libraryInterface.item(item, "values")[0])
        print(ID_Data, 'Open at', self.time_Now)

        #self.c.executemany(f"UPDATE TABLE Data_list SET () WHERE (ID_Data)  ", self.time_Now)
        #self.conn.commit()

        self.Recent_Adding_Backend()

    def Recent_Adding_Backend(self):
        self.Recent_Selection = self.listBook_libraryInterface.selection()
        self.Recent_Data_From_LibraryList = self.listBook_libraryInterface.item(self.Recent_Selection,'values')

        self.RecentItem = [
            (
            self.Recent_Data_From_LibraryList[0], self.Recent_Data_From_LibraryList[1], self.Recent_Data_From_LibraryList[2], self.Recent_Data_From_LibraryList[3], self.Recent_Data_From_LibraryList[4], self.Recent_Data_From_LibraryList[5], self.Recent_Data_From_LibraryList[6]
            )

        ]

        self.c.executemany("INSERT INTO Recent VALUES (?,?,?,?,?,?,?)", self.RecentItem)
        self.conn.commit()

    def Recent_Adding_to_list(self):
        self.c.execute("SELECT * FROM Recent")
        for RecentData in self.c.fetchall():
            self.listRecentBook_HomeInterface.insert("", tk.END, values = (RecentData[0], RecentData[1], RecentData[2], RecentData[3], RecentData[4], RecentData[5], RecentData[6]))
            
    def FavoritAddingBackend(self):
        favoriteList = []
        Dataitem = self.listBook_libraryInterface.selection()
        FavoriteData = (self.listBook_libraryInterface.item(Dataitem, "values"))
        print(FavoriteData[0])

        self.c.execute("SELECT * FROM Favorite")
        for f in self.c.fetchall():
            favoriteList.append(f[0])
        print(favoriteList)
        if FavoriteData[0] in favoriteList:
            print("",end="")
        else:
            FavoriteManyData = [
                    (
                    FavoriteData[0], FavoriteData[1], FavoriteData[2], FavoriteData[3], FavoriteData[4], FavoriteData[5], FavoriteData[6]
                    )
                ]

            self.c.executemany("INSERT INTO Favorite VALUES (?,?,?,?,?,?,?)", FavoriteManyData)
            self.conn.commit()

    def Favorite_Insrerting_Data_to_List(self):
        self.c.execute("SELECT * FROM Favorite")
        
        self.FavoriteItems = self.c.fetchall()

        for FavoriteItem in self.FavoriteItems:
            self.listBook_FavoriteInterface.insert("", tk.END, values = (FavoriteItem[0], FavoriteItem[1], FavoriteItem[2], FavoriteItem[3], FavoriteItem[4], FavoriteItem[5], FavoriteItem[6]))

    def resetApplication(self):
        self.Main_Window.destroy()
        self.__init__()

    def openFileDailog_for_AddFile(self):
        self.Main_Window.filename = tk.filedialog.askopenfilename(initialdir = "/Users/macbook/Documents", title = "Select a pdf file", filetypes = (("pdf files", "*.pdf"),("all files", "*.*")) )

        self.orginalpath = self.Main_Window.filename
        self.destinationPath = "/Users/macbook/Documents/Project/Book_Manager/Data"

        if self.orginalpath != '':
            shutil.move(self.orginalpath, self.destinationPath)
        self.Add_Data_Into_Database()

    def DeleteData_From_FavoriteList(self):
        self.favoriteSelection = self.listBook_FavoriteInterface.selection()
        self.c.execute(f"DELETE FROM Favorite WHERE ID = {self.listBook_FavoriteInterface.item(self.favoriteSelection, 'values')[0]}")
        self.conn.commit()
    
    def ClearRecentListBook_in_Database(self):
        self.c.execute("DELETE FROM Recent")
        self.conn.commit()

if __name__ == "__main__":
    MainfileApplication() 