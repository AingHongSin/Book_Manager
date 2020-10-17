from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import os
from PIL import ImageTk, Image
from tkinter import filedialog
from PyPDF2 import PdfFileReader
import datetime
import sqlite3
import shutil
import Database
import NewAlbum
import FavoriteAdding
from tkmacosx import Button, CircleButton
import subprocess
import AuthorsFunction
import DetailFunction


class MainfileApplication():

    def __init__(self):
                
        self.Main_Window = Tk()
        self.Main_Window.title("My_BooK")
        self.Main_Window.geometry("1210x650+100+100")
        self.Main_Window.resizable(False, False)
        self.Main_Window.config(background = '#00EBFF')

        self.Amount_Book = 0
        self.datalist_of_Database = []
        self.AuthorNameList_Databas = []
        self.Add_Data_Into_Database()
        self.RangeofAuhtorList = 1
        self.ItemList = []
        #self.AuthorFunction()

        # Frame
        self.leftFrame_mainWindow = Frame(self.Main_Window)
        self.leftFrame_mainWindow.pack(side = 'left', fill = 'y')
        self.leftFrame_mainWindow.config(background = ('#98F5FF'))

        #self.topFrame_mainWindow = Frame(self.Main_Window )
        #self.topFrame_mainWindow.pack(side = 'top', fill = 'x')
        #self.topFrame_mainWindow.config(background = '#666666')
        
        self.rightFrame_mainWindow = Frame(self.Main_Window)
        self.rightFrame_mainWindow.pack(fill = 'both', pady = 2, padx = 2, )

            #
        self.LibraryPhoto = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Library.png")
        self.LibraryPotho_image = self.LibraryPhoto.subsample(1,1)

        self.AuthorPhoto = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Authors.png")
        self.AuthorPotho_image = self.AuthorPhoto.subsample(1,1)

        self.CategoriesPhoto = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Category.png")
        self.CategoriesPotho_image = self.CategoriesPhoto.subsample(1,1)

        self.FavoritPhoto = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Favorite.png")
        self.FavoritPhoto_image = self.FavoritPhoto.subsample(1,1)

        self.AlbumPhoto = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Album.png")
        self.AlbumPotho_image = self.AlbumPhoto.subsample(1,1)

        self.AboutPhoto = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/About.png")
        self.AboutPhoto_image = self.AboutPhoto.subsample(1,1)


        # InterFace 
                            # TopFrame
        #self.lblTitle_TopFrame = Label(self.topFrame_mainWindow, text = 'My BooK', height = '2', font = ('defule',36,'bold'), bg = '#666666')
        #self.lblTitle_TopFrame.pack()


                            # LeftFrame

        self.spt_LeftFrame_ridghtSide = ttk.Separator(self.leftFrame_mainWindow, orient = 'vertical')
        self.spt_LeftFrame_ridghtSide.pack(side = 'right' , fill = 'y')

        self.homephoto = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/home.png")
        self.homePhoto_image = self.homephoto.subsample(2,2)

        self.btnHome_leftFrame = Button(self.leftFrame_mainWindow, image = self.homePhoto_image, text = '􀎞', font = ('Comic Sans MS', 16,'bold'), bg = '#98F5FF', activebackground = '#98F5FF', width = 200, border = 10, borderless = 5, borderwidth = 5 ,command = self.homeInterfaceInterface)
        self.btnHome_leftFrame.pack()
        #self.btnHome_leftFrame.configure({"bg": "white", "activebackground": "white"})

        self.spt_leftFrame_topButton = ttk.Separator(self.leftFrame_mainWindow, orient = 'horizontal')
        self.spt_leftFrame_topButton.pack(fill = 'x', pady = 5, padx = 15)

        self.btnLibrary_leftFrame = Button(self.leftFrame_mainWindow, image = self.LibraryPotho_image, text = '\tLibrary\t', border = 0, borderless = 10, borderwidth = 0, compound = 'left', command = self.libraryInterface)
        self.btnLibrary_leftFrame.pack()

        self.btnAuthor_leftFrame = Button(self.leftFrame_mainWindow, image = self.AuthorPotho_image, text = '\tAuthor\t', border = 0, borderless = 10, borderwidth = 0, compound = 'left', command = self.AuthorInterface)
        self.btnAuthor_leftFrame.pack()
        
        ##self.btnCategory_leftFrame = Button(self.leftFrame_mainWindow, image = self.CategoriesPotho_image, text = '\tCategory\t', border = 10, borderless = 10, borderwidth = 0, compound = 'left', command = self.CategoryInterface)
        ##self.btnCategory_leftFrame.pack()

        self.btnFavorit_leftFrame = Button(self.leftFrame_mainWindow, image = self.FavoritPhoto_image, text = '\tFavorite\t', border = 0, borderless = 10, borderwidth = 0,  compound = 'left', command = self.FavoritInterface)
        self.btnFavorit_leftFrame.pack()

        self.btnAlbum_leftFrame = Button(self.leftFrame_mainWindow, image = self.AlbumPotho_image, text = '\tAlbum\t', border = 0, borderless = 10, borderwidth = 0,  compound = 'left', command = self.AlbumInterface)
        self.btnAlbum_leftFrame.pack()

        #eself.btnReport_leftFrame = Button(self.leftFrame_mainWindow , image = self.AboutPhoto_image, text = '\tAbout\t', border = 10, borderless = 10, borderwidth = 0, compound = 'left')
        #eself.btnReport_leftFrame.pack()

        self.spt_leftFrame_UnbderButton = ttk.Separator(self.leftFrame_mainWindow, orient = 'horizontal')
        self.spt_leftFrame_UnbderButton.pack(fill = 'x', pady = 5, padx = 15)

        self.btnExit_leftFrame = Button(self.leftFrame_mainWindow, text = '❌\tExit', border = 10, borderless = 10, borderwidth = 0, height = 50, width = 220, command = self.Main_Window.destroy)
        self.btnExit_leftFrame.pack(side = 'bottom', pady = 1)

        self.spt_leftFrame_TopExitButton = ttk.Separator(self.leftFrame_mainWindow, orient = 'horizontal')
        self.spt_leftFrame_TopExitButton.pack(side = 'bottom', fill = 'x', padx = 15)

        self.homeInterfaceInterface()

        self.Main_Window.mainloop()
        
    def homeInterfaceInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_HomeInterface = Frame(self.rightFrame_mainWindow)
        self.topFrame_HomeInterface.pack( fill = 'x', side = 'top')
        self.topFrame_HomeInterface.config(background = '#00EBFF')


        self.mainFrame_of_Frame_HomeInterface = Frame(self.rightFrame_mainWindow)
        self.mainFrame_of_Frame_HomeInterface.pack(fill = 'x')

        self.AuthorNameFrame_HomeInterface = Frame(self.mainFrame_of_Frame_HomeInterface)
        self.AuthorNameFrame_HomeInterface.pack(side = 'left', fill = 'y')
        self.AuthorNameList_HomeInterface()

        self.AlbumNameFrame_HomeInterface = Frame(self.mainFrame_of_Frame_HomeInterface)
        self.AlbumNameFrame_HomeInterface.pack(side = 'right', fill = 'y')
        self.AlbumList_HomeInterface()

        self.mainFrame_HomeInterface = Frame(self.mainFrame_of_Frame_HomeInterface)
        self.mainFrame_HomeInterface.pack()
    
        self.recentFrame_HomeInterface = Frame(self.rightFrame_mainWindow)
        self.recentFrame_HomeInterface.pack(side = 'bottom')

        self.lblFrame = LabelFrame(self.rightFrame_mainWindow, text = ' Open Recent')
        self.lblFrame.pack( side = 'bottom')

        self.btnLibrary_leftFrame.config(background = 'white')
        self.btnAuthor_leftFrame.config(background = 'white')
        #self.btnCategory_leftFrame.config(background = 'white')
        self.btnAlbum_leftFrame.config(background = 'white')
        self.btnFavorit_leftFrame.config(background = 'white')

        # Interface
                        # Title
        self.lblTitle_HomeIterface = Label(self.topFrame_HomeInterface, text = 'Welcome to\nLibrary Owner', font = ('Apple Chancery',22,'bold'), bg = '#00EBFF')
        self.lblTitle_HomeIterface.pack( fill = 'x', )

        #self.EntSearch_HomeInterface = Entry(self.topFrame_HomeInterface, width = 40)
        #self.EntSearch_HomeInterface.pack()
        #self.EntSearch_HomeInterface.insert("", text = 'Search')

                        # Main

        self.LibraryPhoto_HomeInterface = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Home_Icon/Library@2x.png")
        self.LibraryPotho_image_HomeInterface = self.LibraryPhoto_HomeInterface.subsample(1,1)
        self.btnLibrary_HomeInterface = Button(self.mainFrame_HomeInterface, image = self.LibraryPotho_image_HomeInterface, text = 'Library',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 1, border = 4, command = self.libraryInterface)
        self.btnLibrary_HomeInterface.grid(row = 0, column = 0)

        self.AuthorPhoto_HomeInterface = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Home_Icon/Author@2x.png")
        self.AuthorPotho_image_HomeInterface = self.AuthorPhoto_HomeInterface.subsample(1,1)
        self.btnAuthor_homeInterface = Button(self.mainFrame_HomeInterface, image = self.AuthorPotho_image_HomeInterface, text = 'Authors',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 0, border = 4, command = self.AuthorInterface)
        self.btnAuthor_homeInterface.grid(row = 1, column = 0, columnspan = 2)

        #self.CategoriesPhoto_HomeInterface = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Home_Icon/Category@2x.png")
        #self.CategoriesPotho_image_HomeInterface = self.CategoriesPhoto_HomeInterface.subsample(1,1)
        #self.btnCategory_homeInterface = Button(self.mainFrame_HomeInterface, image = self.CategoriesPotho_image_HomeInterface, text = 'Cateory',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 1, border = 4, command = self.CategoryInterface)
        #self.btnCategory_homeInterface.grid(row = 0, column = 1)

        self.FavoritPhoto_HomeInterface = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Home_Icon/Favorite@2x.png")
        self.FavoritPhoto_image_HomeInterface = self.FavoritPhoto_HomeInterface.subsample(1,1)
        self.btnFavorit_homeInterface = Button(self.mainFrame_HomeInterface, image = self.FavoritPhoto_image_HomeInterface, text = 'Favorite',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 1, border = 4, command = self.FavoritInterface)
        self.btnFavorit_homeInterface.grid(row = 1, column = 1, columnspan = 2)

        self.AlbumPhoto_HomeInterface = PhotoImage(file = r"/Users/privateman/Documents/Project/Book_Manager/icon/Home_Icon/Album@2x.png")
        self.AlbumPotho_image_HomeInterface = self.AlbumPhoto_HomeInterface.subsample(1,1)
        self.btnAlbum_homeInterfac = Button(self.mainFrame_HomeInterface, image = self.AlbumPotho_image_HomeInterface, text = 'Album',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 1, border = 4 , command = self.AlbumInterface)
        self.btnAlbum_homeInterfac.grid(row = 0, column = 2)

        self.btnClearListRecentBook_HomeInterface = Button(self.lblFrame, text = 'Clear Recent', borderless = 10, width = 100, command = self.ClearRecentListBook_in_Database)
        self.btnClearListRecentBook_HomeInterface.pack(anchor = 'ne')

        self.RecentList_HomgInterface()
    
    def AuthorNameList_HomeInterface(self):
        self.lblFrameAuthorName = LabelFrame(self.AuthorNameFrame_HomeInterface, text = 'Author')
        self.lblFrameAuthorName.pack()
        self.tvListName_HomeInterface = ttk.Treeview(self.lblFrameAuthorName, column = ('Author_Name'), show = 'headings', height = 14)
        self.tvListName_HomeInterface.pack(padx = 5, pady = 5)

        self.tvListName_HomeInterface.column('Author_Name', width = '170')
        self.tvListName_HomeInterface.heading('Author_Name', text = 'All Authors')

        self.ShowData_into_Authors_HomeInterface()
        

    def   AlbumList_HomeInterface(self):  
        self.lblFrameAlbumName = LabelFrame(self.AlbumNameFrame_HomeInterface, text = 'Album')
        self.lblFrameAlbumName.pack()
        self.listAllAlbum_AuthorInterface = ttk.Treeview(self.lblFrameAlbumName, show = 'headings', column = ('All_Album'), height = 14)
        self.listAllAlbum_AuthorInterface.pack(padx = 5, pady = 5)

        self.listAllAlbum_AuthorInterface.column('All_Album', width = '170')
        self.listAllAlbum_AuthorInterface.heading('All_Album', text = 'All Album')
        self.ShwoDataIntoListAlbum()


    def RecentList_HomgInterface(self):

        self.listRecentBook_HomeInterface = ttk.Treeview(self.lblFrame, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = 10)
        self.listRecentBook_HomeInterface.pack(pady = 10, padx = 10)

        self.listRecentBook_HomeInterface.column('ID', width = 30)
        self.listRecentBook_HomeInterface.heading('ID', text = 'ID')

        self.listRecentBook_HomeInterface.column('ID', width = 40)
        self.listRecentBook_HomeInterface.heading('ID', text = 'ID')

        self.listRecentBook_HomeInterface.column('Title', width = 250)
        self.listRecentBook_HomeInterface.heading('Title', text = 'Title')

        self.listRecentBook_HomeInterface.column('Author', width = 200)
        self.listRecentBook_HomeInterface.heading('Author', text = 'Author')

        self.listRecentBook_HomeInterface.column('Lenght', width = 120)
        self.listRecentBook_HomeInterface.heading('Lenght', text = 'Length')
    
        self.listRecentBook_HomeInterface.column('Last Readed', width = 160)
        self.listRecentBook_HomeInterface.heading('Last Readed', text = 'Last Readed')

        self.listRecentBook_HomeInterface.column('Date Added', width = 160)
        self.listRecentBook_HomeInterface.heading('Date Added', text = 'Date Added')

        self.Recent_Adding_to_list()

    def libraryInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_LibraryInterface = Frame(self.rightFrame_mainWindow)
        self.topFrame_LibraryInterface.pack(side = 'top', fill = 'x')
        self.topFrame_LibraryInterface.config(background = '#00EBFF')

        self.mainFrame_libraryInterface = Frame(self.rightFrame_mainWindow)
        self.mainFrame_libraryInterface.pack()
        
        # Interface
                            # Tapbar
        self.lblnameTap_libraryInterface = Label(self.topFrame_LibraryInterface, text = 'Library\t\t\t\t', font = ('Times',20,'bold'), bg = '#00EBFF')
        self.lblnameTap_libraryInterface.pack(side = 'right')

        self.btnAddBook_LibraryInterface = Button(self.topFrame_LibraryInterface, text = 'Add', border = 0, borderless = 10, width = 100, height = 30, command = self.openFileDailog_for_AddFile)
        self.btnAddBook_LibraryInterface.pack(side = 'left')

        self.btnDeleteBook_LibraryInterface = Button(self.topFrame_LibraryInterface, text = 'Delete', border = 0, borderless = 10, width = 100, height = 30, command = self.DeleteFile_FromData)
        self.btnDeleteBook_LibraryInterface.pack(side = 'left')      

        self.btnBookDetail_LibraryInterface = Button(self.topFrame_LibraryInterface, text = 'Detail', border = 0, borderless = 10, width = 100, height = 30, command = self.DetailFunction_LibraryInterface)
        self.btnBookDetail_LibraryInterface.pack(side = 'left')   

        self.btnFavoritAdding_LibraryInterface = Button(self.topFrame_LibraryInterface, text = 'Favorit Adding', border = 0, borderless = 10, width = 130, height = 30, command = self.FavoritAddingBackend)
        self.btnFavoritAdding_LibraryInterface.pack(side = 'left')

        self.btnLibrary_leftFrame.config(background = '#3d84a8')
        self.btnAuthor_leftFrame.config(background = 'white')
        #self.btnCategory_leftFrame.config(background = 'white')
        self.btnAlbum_leftFrame.config(background = 'white')
        self.btnFavorit_leftFrame.config(background = 'white')
        
                            # main Interface
        self.listBook_libraryInterface = ttk.Treeview(self.mainFrame_libraryInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '40')
        self.listBook_libraryInterface.pack(padx = '10', pady = '10')
        self.listBook_libraryInterface.bind("<Double-Button-1>", self.openFeature)

        self.listBook_libraryInterface.column('ID', width = '40')
        self.listBook_libraryInterface.heading('ID', text = 'ID')

        self.listBook_libraryInterface.column('Title', width = '250')
        self.listBook_libraryInterface.heading('Title', text = 'Title')

        self.listBook_libraryInterface.column('Author', width = '200')
        self.listBook_libraryInterface.heading('Author', text = 'Author')

        self.listBook_libraryInterface.column('Lenght', width = '120')
        self.listBook_libraryInterface.heading('Lenght', text = 'Length')
    
        self.listBook_libraryInterface.column('Last Readed', width = '170')
        self.listBook_libraryInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_libraryInterface.column('Date Added', width = '170')
        self.listBook_libraryInterface.heading('Date Added', text = 'Date Added')

        #self.listBook_libraryInterface.column('Favorite', width = '80')
        #self.listBook_libraryInterface.heading('Favorite', text = 'Favorite')

        self.library_Data_Adding()


    def AuthorInterface(self):

        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AuthorInterface = Frame(self.rightFrame_mainWindow)
        self.topFrame_AuthorInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AuthorInterface.config(background = '#00EBFF')

        self.listFrame_AuthorInterface = Frame(self.rightFrame_mainWindow)
        self.listFrame_AuthorInterface.pack( pady = 10, padx = 5)

        self.leftFrame_AuthorInterface = Frame(self.listFrame_AuthorInterface)
        self.leftFrame_AuthorInterface.pack(side = 'left', padx = 5)
        #self.leftFrame_AuthorInterface.configure(background = '#c8c8c8')

        self.mainFrame_AuthorInterface = Frame(self.listFrame_AuthorInterface)
        self.mainFrame_AuthorInterface.pack(fill = 'both', padx = 5)

        self.btnAuthor_leftFrame.config(background = '#3d84a8')
        self.btnLibrary_leftFrame.config(background = 'white')
        #self.btnCategory_leftFrame.config(background = 'white')
        self.btnAlbum_leftFrame.config(background = 'white')
        self.btnFavorit_leftFrame.config(background = 'white')

                # Interface

        #self.btnAddBook_AuthorInterface = Button(self.topFrame_AuthorInterface, text = 'Add Author', border = 0, borderless = 10, width = 100, height = 30)
        #self.btnAddBook_AuthorInterface.pack(side = 'left')

        #self.btnDeleteBook_AuthorInterface = Button(self.topFrame_AuthorInterface, text = 'Delete Author', border = 0, borderless = 10, width = 100, height = 30)
        #self.btnDeleteBook_AuthorInterface.pack(side = 'left')      

        #self.btnDeleteBook_AuthorInterface = Button(self.topFrame_AuthorInterface, text = 'Edit Author', border = 0, borderless = 10, width = 100, height = 30)
        #self.btnDeleteBook_AuthorInterface.pack(side = 'left')      
      

        self.lblnameTap_AuthorInterface = Label(self.topFrame_AuthorInterface, text = 'Author', font = ('Times',20,'bold'), bg = '#00EBFF')
        self.lblnameTap_AuthorInterface.pack()

        self.AuthorNameList_AutorInterface()

        self.listBook_AuthorInterface = ttk.Treeview(self.mainFrame_AuthorInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '40')
        self.listBook_AuthorInterface.pack()
        self.listBook_AuthorInterface.bind("<Double-Button-1>", self.openFeature_inAuthorInterface)

        self.listBook_AuthorInterface.column('ID', width = '30')
        self.listBook_AuthorInterface.heading('ID', text = 'ID')

        self.listBook_AuthorInterface.column('Title', width = '200')
        self.listBook_AuthorInterface.heading('Title', text = 'Title')

        self.listBook_AuthorInterface.column('Author', width = '140')
        self.listBook_AuthorInterface.heading('Author', text = 'Author')

        self.listBook_AuthorInterface.column('Lenght', width = '75')
        self.listBook_AuthorInterface.heading('Lenght', text = 'Length')
    
        self.listBook_AuthorInterface.column('Last Readed', width = '160')
        self.listBook_AuthorInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_AuthorInterface.column('Date Added', width = '160')
        self.listBook_AuthorInterface.heading('Date Added', text = 'Date Added')
        
        #self.listBook_AuthorInterface.column(7, width = '100')
        #self.listBook_AuthorInterface.heading(7, text = 'Favorite')


    def AuthorNameList_AutorInterface(self):

        self.tvListName_AuthorInterface = ttk.Treeview(self.leftFrame_AuthorInterface, column = ('Author_Name'), show = 'headings', height = 40)
        self.tvListName_AuthorInterface.pack()
        self.tvListName_AuthorInterface.bind("<Double-Button-1>", self.OnDoubleClick_Author)

        self.tvListName_AuthorInterface.column('Author_Name', width = '200')
        self.tvListName_AuthorInterface.heading('Author_Name', text = 'All Authors')

        self.ShowData_into_Authors_AuthorInterface()
        
    def FavoritInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()
        # Frame
        self.topFrame_FavoriteInterface = Frame(self.rightFrame_mainWindow)
        self.topFrame_FavoriteInterface.pack(side = 'top', fill = 'x')
        self.topFrame_FavoriteInterface.config(background = '#00EBFF')
        
        self.mainFrame_FevoriteInterface = Frame(self.rightFrame_mainWindow)
        self.mainFrame_FevoriteInterface.pack(fill = 'both')
        
        # Interface
                            # Tapbar
        self.lblnameTap_FavoriteInterface = Label(self.topFrame_FavoriteInterface, text = 'Favorite\t\t\t\t\t\t', border = 0, font = ('Times',20,'bold'), bg = '#00EBFF')
        self.lblnameTap_FavoriteInterface.pack(side = 'right')

        self.btnAddBook_FavoriteInterface = Button(self.topFrame_FavoriteInterface, text = 'Add', border = 0, borderless = 10, width = 100, height = 30, command = self.FavoriteAdding_Function)
        self.btnAddBook_FavoriteInterface.pack(side = 'left')

        self.btnDeleteBook_FavoriteInterface = Button(self.topFrame_FavoriteInterface, text = 'Delete', border = 0, borderless = 10, width = 100, height = 30, command = self.DeleteData_From_FavoriteList)
        self.btnDeleteBook_FavoriteInterface.pack(side = 'left')     

        self.btnAuthor_leftFrame.config(background = 'white')
        self.btnLibrary_leftFrame.config(background = 'white')
        #self.btnCategory_leftFrame.config(background = 'white')
        self.btnAlbum_leftFrame.config(background = 'white')
        self.btnFavorit_leftFrame.config(background = '#3d84a8')

                            # main Interface
        self.listBook_FavoriteInterface = ttk.Treeview(self.mainFrame_FevoriteInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '40')
        self.listBook_FavoriteInterface.pack(padx = '10', pady = '10')
        self.listBook_FavoriteInterface.bind("<Double-Button-1>" , self.FileOpening_in_FavoriteInterface)
        self.listBook_FavoriteInterface.tag_configure('odd', background='#E8E8E8')
        self.listBook_FavoriteInterface.tag_configure('even', background='#DFDFDF')

        self.listBook_FavoriteInterface.column('ID', width = '40')
        self.listBook_FavoriteInterface.heading('ID', text = 'ID')

        self.listBook_FavoriteInterface.column('Title', width = '250')
        self.listBook_FavoriteInterface.heading('Title', text = 'Title')

        self.listBook_FavoriteInterface.column('Author', width = '200')
        self.listBook_FavoriteInterface.heading('Author', text = 'Author')

        self.listBook_FavoriteInterface.column('Lenght', width = '120')
        self.listBook_FavoriteInterface.heading('Lenght', text = 'Length')
    
        self.listBook_FavoriteInterface.column('Last Readed', width = '170')
        self.listBook_FavoriteInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_FavoriteInterface.column('Date Added', width = '170')
        self.listBook_FavoriteInterface.heading('Date Added', text = 'Date Added')

        for row in self.listBook_FavoriteInterface.get_children():
            self.listBook_FavoriteInterface.delete(row)

        self.Favorite_Insrerting_Data_to_List()

    def AlbumInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AlbumInterface = Frame(self.rightFrame_mainWindow)
        self.topFrame_AlbumInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AlbumInterface.config(background = '#00EBFF')

        self.listFrame_AlbumInterface = Frame(self.rightFrame_mainWindow)
        self.listFrame_AlbumInterface.pack(pady = 10, padx = 5)

        self.leftFrame_AlbumInterface = Frame(self.listFrame_AlbumInterface)
        self.leftFrame_AlbumInterface.pack(side = 'left', fill = 'y', padx = 5)

        self.mainFrame_AlbumInterface = Frame(self.listFrame_AlbumInterface)
        self.mainFrame_AlbumInterface.pack(fill = 'both', padx = 5)

        # Interface
        self.btnAddBook_AlbumInterface = Button(self.topFrame_AlbumInterface, text = 'Add Album', border = 0, borderless = 10, width = 100, height = 30, command = NewAlbum.NewAlbumAction)
        self.btnAddBook_AlbumInterface.pack(side = 'left')

        self.btnDeleteBook_AlbumInterface = Button(self.topFrame_AlbumInterface, text = 'Delete Album', border = 0, borderless = 10, width = 100, height = 30, command = self.DeleteData_from_list_and_Database)
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.btnDeleteBook_AlbumInterface = Button(self.topFrame_AlbumInterface, text = 'Edit Album', border = 0, borderless = 10, width = 100, height = 30)
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.lblnameTap_AlbumInterface = Label(self.topFrame_AlbumInterface, text = 'Album\t\t\t\t\t', font = ('Times',20,'bold'), bg = '#00EBFF')
        self.lblnameTap_AlbumInterface.pack(side = 'right')

        self.btnLibrary_leftFrame.config(background = 'white')
        self.btnAuthor_leftFrame.config(background = 'white')
        #self.btnCategory_leftFrame.config(background = 'white')
        self.btnAlbum_leftFrame.config(background = '#3d84a8')
        self.btnFavorit_leftFrame.config(background = 'white')

        self.AlbumList_AlbumInterface()

        self.listBook_AlbumInterface = ttk.Treeview(self.mainFrame_AlbumInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = 40)
        self.listBook_AlbumInterface.pack()
        self.listBook_AlbumInterface.bind("<Double-Button-1>", self.OpenFunction_fromAlbumInterface)

        self.listBook_AlbumInterface.column('ID', width = '30')
        self.listBook_AlbumInterface.heading('ID', text = 'ID')

        self.listBook_AlbumInterface.column('Title', width = '200')
        self.listBook_AlbumInterface.heading('Title', text = 'Title')

        self.listBook_AlbumInterface.column('Author', width = '140')
        self.listBook_AlbumInterface.heading('Author', text = 'Author')

        self.listBook_AlbumInterface.column('Lenght', width = '75')
        self.listBook_AlbumInterface.heading('Lenght', text = 'Length')
    
        self.listBook_AlbumInterface.column('Last Readed', width = '160')
        self.listBook_AlbumInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_AlbumInterface.column('Date Added', width = '160')
        self.listBook_AlbumInterface.heading('Date Added', text = 'Date Added')
        
    def AlbumList_AlbumInterface(self):
        self.listAllAlbum_AuthorInterface = ttk.Treeview(self.leftFrame_AlbumInterface, show = 'headings', column = ('All_Album'), height = 40)
        self.listAllAlbum_AuthorInterface.pack()

        self.listAllAlbum_AuthorInterface.column('All_Album', width = '200')
        self.listAllAlbum_AuthorInterface.heading('All_Album', text = 'All Album')
        self.listAllAlbum_AuthorInterface.bind("<Double-Button-1>", self.AlbumSelection_and_ShowData_in_DataList)
        self.ShwoDataIntoListAlbum()
#___________________________________________________________________________________________BACK-END__________________________________________________________________#

    def Add_Data_Into_Database(self):
        # Database
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Data_list ")
        self.items = self.c.fetchall()

        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Data')
        self.dataFromDataFolder = os.listdir()

        for item in self.items:
            self.datalist_of_Database.append(item[1])

        self.Amount_Book = len(self.items) + 1

        for self.row in self.dataFromDataFolder:
            if self.row != '.DS_Store':
                if self.row in self.datalist_of_Database:
                    print("", end="")
                else:
                    pdf_path = str(self.row)
                    with open(pdf_path, 'rb') as f:
                        self.pdf = PdfFileReader(f)
                        self.information = self.pdf.getDocumentInfo()
                        self.number_of_pages = self.pdf.getNumPages()

                    ID = self.Amount_Book 
                    Title = str(self.row)
                    Author = (self.information.author)
                    Number_of_Pages = (self.number_of_pages)
                    Last_Read = ('Unknown ')
                    Add_Date = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d  %H:%M:%S"))

                    if Author == None:
                        libraryData = [
                                    (ID, Title, 'Unkonwn Author', Number_of_Pages, Last_Read, Add_Date)
                                    ]

                        self.c.executemany("INSERT INTO Data_list VALUES (?,?,?,?,?,?)" , libraryData)
                        self.conn.commit()
                        self.Amount_Book += 1
                    else: 
                        libraryData = [
                                    (ID, Title, Author, Number_of_Pages, Last_Read, Add_Date)
                                    ]

                        self.c.executemany("INSERT INTO Data_list VALUES (?,?,?,?,?,?)" , libraryData)
                        self.conn.commit()
                        self.Amount_Book += 1
                    
                    self.conn.commit()
                    self.conn.close()
                    AuthorsFunction.Function(ID, Title, Author, Number_of_Pages, Last_Read, Add_Date)

    def library_Data_Adding(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Data_list ")
        self.items = self.c.fetchall()

        for item in self.items:
            if item[2] == None:
                self.listBook_libraryInterface.insert("", END, values = (int(item[0]), item[1], 'Unknown Author', item[3],  item[4], item[5] ))
            else: 
                self.listBook_libraryInterface.insert("", END, values = (int(item[0]), item[1], item[2], item[3],  item[4], item[5] ))
            
            #if int(item[0]) % 2 == 0:
            #    self.listBook_libraryInterface.configure(even, background = 'blue')


        self.conn.close()

    #def select(self, event=None):
        self.listBook_libraryInterface.selection_toggle(self.listBook_libraryInterface.focus())
        print(self.listBook_libraryInterface.selection())

    def FileOpening_in_FavoriteInterface(self, event):
        item = self.listBook_FavoriteInterface.selection()
        Name_Data = str(self.listBook_FavoriteInterface.item(item, "values")[1])

        FileName = ("/Users/privateman/Documents/Project/Book_Manager/Data/" + Name_Data)
        subprocess.call(['open', FileName])
        self.Recent_Adding_Backend_fromFavorite()

    def Recent_Adding_Backend_fromFavorite(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.Recent_Selection = self.listBook_FavoriteInterface.selection()
        self.Recent_Data_From_FavoriteList = self.listBook_FavoriteInterface.item(self.Recent_Selection,'values')

        self.RecentItem = [
            (
            self.Recent_Data_From_FavoriteList[0], self.Recent_Data_From_FavoriteList[1], self.Recent_Data_From_FavoriteList[2], self.Recent_Data_From_FavoriteList[3], self.Recent_Data_From_FavoriteList[4], self.Recent_Data_From_FavoriteList[5]
            )
        ]

        self.c.executemany("INSERT INTO Recent VALUES (?,?,?,?,?,?)", self.RecentItem)
        self.conn.commit()
        self.conn.close()

    def OpenFunction_fromAlbumInterface(self, event):

        item = self.listBook_AlbumInterface.selection()
        Name_Data = str(self.listBook_AlbumInterface.item(item, "values")[1])

        FileName = ("/Users/privateman/Documents/Project/Book_Manager/Data/" + Name_Data)
        subprocess.call(['open', FileName])

        self.Recent_Adding_Backend_fromAlbum()

    def Recent_Adding_Backend_fromAlbum(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()


        self.Recent_Selection = self.listBook_AlbumInterface.selection()
        self.Recent_Data_From_AlbumList = self.listBook_AlbumInterface.item(self.Recent_Selection,'values')

        self.RecentItem = [
            (
            self.Recent_Data_From_AlbumList[0], self.Recent_Data_From_AlbumList[1], self.Recent_Data_From_AlbumList[2], self.Recent_Data_From_AlbumList[3], self.Recent_Data_From_AlbumList[4], self.Recent_Data_From_AlbumList[5]
            )
        ]

        self.c.executemany("INSERT INTO Recent VALUES (?,?,?,?,?,?)", self.RecentItem)
        self.conn.commit()
        self.conn.close()

    def openFeature(self, event):
        ot = []
        ND = []

        time_Now = (datetime.datetime.now().astimezone().strftime("%Y/%m/%d  %H:%M:%S"))
        ot.append(time_Now)
        item = self.listBook_libraryInterface.selection()
        Name_Data = str(self.listBook_libraryInterface.item(item, "values")[1])
        print(Name_Data, 'Open at', time_Now)
        ND.append(Name_Data)
        print(ND[0:])

        FileName = ("/Users/privateman/Documents/Project/Book_Manager/Data/" + Name_Data)
        subprocess.call(['open', FileName])
        print(ot)
        #self.c.execute(f"UPDATE Data_list SET Last_Readded = {ot} WHERE Title = {ND[0:]}" )
        #self.conn.commit()

        self.Recent_Adding_Backend_fromLibrary()

    def Recent_Adding_Backend_fromLibrary(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.Recent_Selection = self.listBook_libraryInterface.selection()
        self.Recent_Data_From_LibraryList = self.listBook_libraryInterface.item(self.Recent_Selection,'values')

        self.RecentItem = [
            (
            self.Recent_Data_From_LibraryList[0], self.Recent_Data_From_LibraryList[1], self.Recent_Data_From_LibraryList[2], self.Recent_Data_From_LibraryList[3], self.Recent_Data_From_LibraryList[4], self.Recent_Data_From_LibraryList[5]
            )
        ]

        self.c.executemany("INSERT INTO Recent VALUES (?,?,?,?,?,?)", self.RecentItem)
        self.conn.commit()
        self.conn.close()

    def Recent_Adding_to_list(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        for row in self.listRecentBook_HomeInterface.get_children():
            self.listRecentBook_HomeInterface.delete(row)

        self.c.execute("SELECT * FROM Recent")
        for RecentData in self.c.fetchall():
            self.listRecentBook_HomeInterface.insert("", 0, values = (RecentData[0], RecentData[1], RecentData[2], RecentData[3], RecentData[4], RecentData[5]))

        self.conn.close()

    def FavoriteAdding_Function(self):
        FavoriteAdding.FavoriteAdding_from_Library()
        self.FavoritInterface()

    def FavoritAddingBackend(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        favoriteList = []
        Dataitem = self.listBook_libraryInterface.selection()
        FavoriteData = (self.listBook_libraryInterface.item(Dataitem, "values"))
        print('Data in Library for check...', FavoriteData[0])

        FD = int(FavoriteData[0])
        self.c.execute("SELECT * FROM Favorite")
        for f in self.c.fetchall():
            favoriteList.append(f[0])
        print('Data in Favorite Datalist', favoriteList)
        if FD in favoriteList:
            print('Loading Please wait ...')
            tkinter.messagebox.showerror('Error', 'This book already have in Favorite Library')
        else:
            if FavoriteData[0] != favoriteList:
                FavoriteManyData = [
                        (
                        FavoriteData[0], FavoriteData[1], FavoriteData[2], FavoriteData[3], FavoriteData[4], FavoriteData[5]
                        )
                    ]

                self.c.executemany("INSERT INTO Favorite VALUES (?,?,?,?,?,?)", FavoriteManyData)
                self.conn.commit()
                self.conn.close()

    def Favorite_Insrerting_Data_to_List(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Favorite")
        
        self.FavoriteItems = self.c.fetchall()

        for FavoriteItem in self.FavoriteItems:
            self.listBook_FavoriteInterface.insert("", END, values = (FavoriteItem[0], FavoriteItem[1], FavoriteItem[2], FavoriteItem[3], FavoriteItem[4], FavoriteItem[5]))
        self.conn.close()

    def openFileDailog_for_AddFile(self):
        self.Main_Window.filename = filedialog.askopenfilename(initialdir = "/Users/privateman/Documents", title = "Select a pdf file", filetypes = (("pdf files", "*.pdf"),("all files", "*.*")) )

        self.orginalpath = self.Main_Window.filename
        self.destinationPath = "/Users/privateman/Documents/Project/Book_Manager/Data"

        if self.orginalpath != '':
            shutil.copy(self.orginalpath, self.destinationPath)
        print("Adding...")
        self.Add_Data_Into_Database()
        #self.AuthorFunction()
        self.libraryInterface()

    def DeleteData_From_FavoriteList(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.favoriteSelection = self.listBook_FavoriteInterface.selection()
        self.c.execute(f"DELETE FROM Favorite WHERE ID = {self.listBook_FavoriteInterface.item(self.favoriteSelection, 'values')[0]}")
        self.conn.commit()
        self.conn.close()
        self.FavoritInterface()
    
    def ClearRecentListBook_in_Database(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("DELETE FROM Recent")
        self.conn.commit()
        self.conn.close()
        self.Recent_Adding_to_list()

    def ShwoDataIntoListAlbum(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Album")
        for AlbumNameList in self.c.fetchall():
            self.listAllAlbum_AuthorInterface.insert("", END, values = (AlbumNameList))
        
        self.conn.close()

    def AlbumSelection_and_ShowData_in_DataList(self, event):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        for row in self.listBook_AlbumInterface.get_children():
            self.listBook_AlbumInterface.delete(row)
        AlbumSelection = self.listAllAlbum_AuthorInterface.selection()
        SelectionItem_Album = self.listAllAlbum_AuthorInterface.item(AlbumSelection, 'values')[0]

        self.c.execute(f"SELECT  * from [{SelectionItem_Album}]")
        for AlbumData in self.c.fetchall():
            self.listBook_AlbumInterface.insert("", END, values = (AlbumData[0], AlbumData[1], AlbumData[2], AlbumData[3], AlbumData[4], AlbumData[5]))

        self.conn.close()

    def DeleteData_from_list_and_Database(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.AlbumDeleting = []
        self.AlbumSelection = self.listAllAlbum_AuthorInterface.focus()
        SelectionItem_Album = str(self.listAllAlbum_AuthorInterface.item(self.AlbumSelection, 'values')[0])
        self.AlbumDeleting.append(SelectionItem_Album)
        self.ALbumDataList = []
        self.c.execute("SELECT * FROM Album")
        for g in self.c.fetchall():
            self.ALbumDataList.append(g[0])

        if SelectionItem_Album in self.ALbumDataList:
            self.c.execute(f"DELETE FROM Album WHERE Album_NameList = (?)", self.AlbumDeleting)
            self.conn.commit()
            self.c.execute(f"DROP TABLE [{SelectionItem_Album}]")
            self.conn.commit()
            self.AlbumInterface()
        self.conn.close()

    def AddCategory_Into_CategoryNameList(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')  
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Categories")
        for self.h in self.c.fetchall():
            self.tvListCategory_CategorInterface.insert("", END, values = (self.h))
        self.conn.close()

    def ShowCategories_in_DataList(self, event):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        for row in self.listBook_CategoryInterface.get_children():
            self.listBook_CategoryInterface.delete(row)
        d = self.tvListCategory_CategorInterface.selection()
        Selection_Category = self.tvListCategory_CategorInterface.item(d, 'values')[0]

        self.c.execute(f"SELECT * FROM {Selection_Category}")
        for CategoriesData in self.c.fetchall():
            self.listBook_CategoryInterface.insert("", END, values = (CategoriesData[0], CategoriesData[1], CategoriesData[2], CategoriesData[3], CategoriesData[4], CategoriesData[5]))
        
        self.conn.close()


    def ShowData_into_Authors_AuthorInterface(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Authors")
        for h in self.c.fetchall():
            if h == None:
                self.tvListName_AuthorInterface.insert("", END, values = ('Unknown Author'))
            else:
                self.tvListName_AuthorInterface.insert("", END, values = (h))
        self.conn.close()

    def ShowData_into_Authors_HomeInterface(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Authors")
        for h in self.c.fetchall():
            self.tvListName_HomeInterface.insert("", END, values = (h))

        self.conn.close()

    def OnDoubleClick_Author(self, event):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        for row in self.listBook_AuthorInterface.get_children():
            self.listBook_AuthorInterface.delete(row)

        item = self.tvListName_AuthorInterface.selection()
        print("This is ", str(self.tvListName_AuthorInterface.item(item ,"values")[0]))

        AuthorsNameItem = self.tvListName_AuthorInterface.item(item ,"values")[0]

        self.c.execute(f"SELECT * FROM [{AuthorsNameItem}]")
        for AuthorData_into_AuthorsNameList in self.c.fetchall():
            self.listBook_AuthorInterface.insert("", END, values = (AuthorData_into_AuthorsNameList[0], AuthorData_into_AuthorsNameList[1], AuthorData_into_AuthorsNameList[2], AuthorData_into_AuthorsNameList[3], AuthorData_into_AuthorsNameList[4], AuthorData_into_AuthorsNameList[5]))
        self.conn.close()
    
    def openFeature_inAuthorInterface(self, event):
        ot = []
        ND = []

        time_Now = (datetime.datetime.now().astimezone().strftime("%Y/%m/%d  %H:%M:%S"))
        ot.append(time_Now)
        item = self.listBook_AuthorInterface.selection()
        Name_Data = str(self.listBook_AuthorInterface.item(item, "values")[1])
        print(Name_Data, 'Open at', time_Now)
        ND.append(Name_Data)
        print(ND[0:])

        FileName = ("/Users/privateman/Documents/Project/Book_Manager/Data/" + Name_Data)
        subprocess.call(['open', FileName])
        print(ot)
        self.Recent_Adding_Backend_fromAuthors_Inyterface()

    def Recent_Adding_Backend_fromAuthors_Inyterface(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.Recent_Selection = self.listBook_AuthorInterface.selection()
        self.Recent_Data_From_AuthorList = self.listBook_AuthorInterface.item(self.Recent_Selection,'values')

        self.RecentItem = [
            (
            self.Recent_Data_From_AuthorList[0], self.Recent_Data_From_AuthorList[1], self.Recent_Data_From_AuthorList[2], self.Recent_Data_From_AuthorList[3], self.Recent_Data_From_AuthorList[4], self.Recent_Data_From_AuthorList[5],
            )
        ]

        self.c.executemany("INSERT INTO Recent VALUES (?,?,?,?,?,?)", self.RecentItem)
        self.conn.commit()
        self.conn.close()        

    def DeleteFile_FromData(self):
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Data')

        self.SelectionItemfromList = self.listBook_libraryInterface.selection()
        self.NameSelectionItem = self.listBook_libraryInterface.item(self.SelectionItemfromList, 'values')[1]
        self.IDSelectionItem = self.listBook_libraryInterface.item(self.SelectionItemfromList, 'values')[0]

        os.remove(f"{self.NameSelectionItem}")

        self.deleteDatafromDatabase(self.NameSelectionItem)

    def deleteDatafromDatabase(self, IDSelection):
        IDSelectionItem = str(IDSelection)
        tabelinDatabase = []

        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute('SELECT name from sqlite_master where type = "table"')
        for items in self.c.fetchall():
            print(items[0])
            tabelinDatabase.append(items[0])
        
        for t in range(len(tabelinDatabase)):
            o = str(tabelinDatabase[t])

            print("= O => ",o)
            tabelinDatabase[t] = []
            self.c.execute(f"SELECT * FROM [{o}]")
            for k in self.c.fetchall():
                tabelinDatabase[t].append(k[1])
                
            print("t=>",tabelinDatabase[t])
        
            print("IDSelectionItem-->",IDSelectionItem[0:])
            print("->", o)
            if IDSelectionItem in tabelinDatabase[t]:
                print("-------")
                dt = []
                ID  = [IDSelectionItem]
                self.c.execute(f"DELETE FROM [{o}] WHERE Title = (?)", ID[0:] )
                self.conn.commit()
                print("-----------------------Deleted Sucessfully!-----------------------")
                
                self.c.execute(f"SELECT * FROM [{o}]")
                for y in self.c.fetchall():
                    dt.append(y[0])
                if dt == []:
                    if o != 'Album' and o != 'Favorite' and  o != 'Recent' and o != 'Data_list' and o != 'Authors':
                        self.c.execute(f"DROP TABLE [{o}]")
                        self.conn.commit()

                        rt = [o]
                        self.c.execute("DELETE FROM Authors WHERE Authors_NameList = (?)", rt[0:])
                        self.conn.commit()

                        at = [o]
                        self.c.execute("DELETE FROM Album WHERE Album_NameList = (?)", at[0:])
                        self.conn.commit()
                        
            print()
        
        self.conn.commit()
        self.conn.close() 
        self.libraryInterface()

    def DetailFunction_LibraryInterface(self):
        selectItem = self.listBook_libraryInterface.selection()
        Name = self.listBook_libraryInterface.item(selectItem, 'values')[1]
        
        print(Name)
        
        os.chdir('/Users/privateman/Documents/Project/Book_Manager/Data')

        pdf_path = str(Name)

        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
        
        Title =  (information.title)
        Author =  (information.author)
        Creator =  (information.creator)
        Producer =  (information.producer)
        Subject =  (information.subject)
        Number_of_pages =  (number_of_pages)

        if Title == '':
            Title = 'Unknown Title'
        elif Author == '':
            Author = 'Unknown Author'
        elif Creator == '':
            Creator = 'Unknown Creator'
        elif Producer == '':
            Producer = 'Unknown Producer'
        elif Subject == '':
            Subject = 'Unknown Subject'


        print('Name :', Name)
        print('Title :', Title)
        print('Author :', Author)
        print('Creator :', Creator)
        print('Producer :', Producer)
        print('Subject :', Subject)
        print('Page :', Number_of_pages)


        DetailFunction.DetailFunction(Name, Title, Author, Creator, Producer, Subject, Number_of_pages)


if __name__ == "__main__":
    MainfileApplication() 