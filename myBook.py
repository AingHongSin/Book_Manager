    #from CreateDatabase import change_dir
import datetime
import os
    #import fitz
    #import shutil
import sqlite3
import subprocess
    #import tkinter.messagebox

from contextlib import contextmanager
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from tkmacosx import Button
from tkmacosx.widget import CircleButton 

import LibraryInterfaceaInList
import LibraryInterfaceInGird
import ExtractMetadaFromPDF
    #import AuthorsFunction
    #import Convert_fomPdf_toImage
import CreateDatabase
    #import DetailFunction
import EditAlbumFuntion
import FavoriteAdding
    #import Database
import NewAlbum
    #from PyPDF2 import PdfFileReader

#import ImageExtraction


class MainfileApplication():

    def __init__(self):
                

        self.Main_Window = Tk()
        self.Main_Window.title("My_BooK")
        self.Main_Window.geometry("1220x690+100+100")
        #self.Main_Window.resizable(False, False)
        self.Main_Window.config(background = '#00EBFF')
        self.Main_Window.attributes('-alpha', 1)
        #self.Main_Window.attributes('-transparent', True)
        #self.Main_windown.config(background = 'systemTransparent')
        #self.Main_Window.attributes('-transparentcolor','blue')
        #self.Main_Window.overrideredirect(True)
        #with self.change_dir('icon'):
        #    photo = ttk.PhotoImage(file = "mybookLogo.ico")
        #    self.Main_Window.iconphoto(True, photo)

        CreateDatabase.CreateDatabaseFunction()
        ExtractMetadaFromPDF.Extract_Metada_From_PDF()


            # Global Variabel
        self.Amount_Book = 0
        self.AuthorNameList_Databas = []

        self.RangeofAuhtorList = 1
        self.ItemList = []
        
        self.btnList = True
                

        #self.AuthorFunction()

        # Frame
        self.leftFrame_mainWindow = Frame(self.Main_Window)
        self.leftFrame_mainWindow.pack(side = 'left', fill = 'y')
        self.leftFrame_mainWindow.config(background = ('#98F5FF'))

        #self.topFrame_mainWindow = Frame(self.Main_Window )
        #self.topFrame_mainWindow.pack(side = 'top', fill = 'x')
        #self.topFrame_mainWindow.config(background = '#666666')
        
        self.holdrightFrame_mainwindow = Frame(self.Main_Window)
        self.holdrightFrame_mainwindow.pack(fill = 'both', pady = 2, padx = 2,)
        
        self.ToprightFrame_mianwindow = Frame(self.holdrightFrame_mainwindow, bg = 'red')
        self.ToprightFrame_mianwindow.pack(fill = 'x', side = 'top')
        
        self.rightFrame_mainWindow = Frame(self.holdrightFrame_mainwindow)
        self.rightFrame_mainWindow.pack(fill = 'x' )

            #
        with self.change_dir('Resourse/icon'):
            self.homePhoto_Patch = (os.getcwd() + "/" + "mybook.png")
            self.homephoto = PhotoImage(file = self.homePhoto_Patch)
            self.homePhoto_image = self.homephoto.subsample(1,1)

            self.LibraryPhoto_Patch = (os.getcwd() + "/" + "Library.png")
            self.LibraryPhoto = PhotoImage(file = self.LibraryPhoto_Patch)
            self.LibraryPotho_image = self.LibraryPhoto.subsample(1,1)

            self.AuthorPhoto_Patch = (os.getcwd() + "/" + "Authors.png")
            self.AuthorPhoto = PhotoImage(file = self.AuthorPhoto_Patch)
            self.AuthorPotho_image = self.AuthorPhoto.subsample(1,1)

            self.FavoritePhoto_Patch = (os.getcwd() + "/" + "Favorite.png")
            self.FavoritPhoto = PhotoImage(file = self.FavoritePhoto_Patch)
            self.FavoritPhoto_image = self.FavoritPhoto.subsample(1,1)

            self.AlbumPhoto_Patch = (os.getcwd() + "/" + "Album.png")
            self.AlbumPhoto = PhotoImage(file = self.AlbumPhoto_Patch)
            self.AlbumPotho_image = self.AlbumPhoto.subsample(1,1)

            self.AboutPhoto_Patch = (os.getcwd() + "/" + "About.png")
            self.AboutPhoto = PhotoImage(file = self.AboutPhoto_Patch)
            self.AboutPhoto_image = self.AboutPhoto.subsample(1,1)


        # InterFace 
                            # TopFrame
        #self.lblTitle_TopFrame = Label(self.topFrame_mainWindow, text = 'My BooK', height = '2', font = ('defule',36,'bold'), bg = '#666666')
        #self.lblTitle_TopFrame.pack()


                            # LeftFrame

        self.spt_LeftFrame_ridghtSide = ttk.Separator(self.leftFrame_mainWindow, orient = 'vertical')
        self.spt_LeftFrame_ridghtSide.pack(side = 'right' , fill = 'y')

        self.btnHome_leftFrame = Button(self.leftFrame_mainWindow, image = self.homePhoto_image, bg = '#98F5FF', activebackground = '#98F5FF', width = 220, border = 10, borderless = 5, borderwidth = 5, command = self.homeInterfaceInterface)
        self.btnHome_leftFrame.pack()
        #self.btnHome_leftFrame.configure({"bg": "white", "activebackground": "white"})

        self.spt_leftFrame_topButton = ttk.Separator(self.leftFrame_mainWindow, orient = 'horizontal')
        self.spt_leftFrame_topButton.pack(fill = 'x', pady = 5, padx = 15)

        self.btnLibrary_leftFrame = Button(self.leftFrame_mainWindow, image = self.LibraryPotho_image, text = '\tLibrary\t', border = 10, borderless = 10, borderwidth = 0, compound = 'left', height = 45, command = self.libraryInterface)
        self.btnLibrary_leftFrame.pack()

        self.btnAuthor_leftFrame = Button(self.leftFrame_mainWindow, image = self.AuthorPotho_image, text = '\tAuthor\t', border = 10, borderless = 10, borderwidth = 0, compound = 'left', height = 45, command = self.AuthorInterface)
        self.btnAuthor_leftFrame.pack()

        self.btnFavorit_leftFrame = Button(self.leftFrame_mainWindow, image = self.FavoritPhoto_image, text = '\tFavorite\t', border = 10, borderless = 10, borderwidth = 0,  compound = 'left', height = 45, command = self.FavoritInterface)
        self.btnFavorit_leftFrame.pack()

        self.btnAlbum_leftFrame = Button(self.leftFrame_mainWindow, image = self.AlbumPotho_image, text = '\tAlbum\t', border = 10, borderless = 10, borderwidth = 0,  compound = 'left', height = 45, command = self.AlbumInterface)
        self.btnAlbum_leftFrame.pack()

        #eself.btnReport_leftFrame = Button(self.leftFrame_mainWindow , image = self.AboutPhoto_image, text = '\tAbout\t', border = 10, borderless = 10, borderwidth = 0, compound = 'left')
        #eself.btnReport_leftFrame.pack()

        self.spt_leftFrame_UnbderButton = ttk.Separator(self.leftFrame_mainWindow, orient = 'horizontal')
        self.spt_leftFrame_UnbderButton.pack(fill = 'x', pady = 5, padx = 15)

        self.btnExit_leftFrame = Button(self.leftFrame_mainWindow, text = '❌\tExit', border = 10, borderless = 10, borderwidth = 0, height = 50, width = 220, command = self.Main_Window.destroy)
        self.btnExit_leftFrame.pack(side = 'bottom', pady = 5)

        self.spt_leftFrame_TopExitButton = ttk.Separator(self.leftFrame_mainWindow, orient = 'horizontal')
        self.spt_leftFrame_TopExitButton.pack(side = 'bottom', fill = 'x', padx = 15)
        
        self.btnListAndGrid_mainrightFrame  = CircleButton(self.ToprightFrame_mianwindow, text = '􀋲', borderless = 10, border = 10, borderwidth = 0, height = 60, bg = 'lime', command = self.ConfiguringListandGrid)
        self.btnListAndGrid_mainrightFrame.pack(side = 'left')
        
    
        self.homeInterfaceInterface()

        self.Main_Window.mainloop()
        
    def homeInterfaceInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        
        
        self.Library = False
        self.Author = False
        self.Favorite = False
        self.Album = False




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
        self.lblTitle_HomeIterface = Label(self.topFrame_HomeInterface, text = 'myBook\nYour own Library in Your hands', font = ('Apple Chancery',22,'bold'), bg = '#00EBFF')
        self.lblTitle_HomeIterface.pack( fill = 'x', )

        #self.EntSearch_HomeInterface = Entry(self.topFrame_HomeInterface, width = 40)
        #self.EntSearch_HomeInterface.pack()
        #self.EntSearch_HomeInterface.insert("", text = 'Search')

                        # Main
        with self.change_dir('Resourse/icon/Home_Icon'):
            self.LibraryPhoto_HomeInterface = PhotoImage(file = (os.getcwd() + "/" + "Library@2x.png"))
            self.LibraryPotho_image_HomeInterface = self.LibraryPhoto_HomeInterface.subsample(1,1)
            self.btnLibrary_HomeInterface = Button(self.mainFrame_HomeInterface, image = self.LibraryPotho_image_HomeInterface, text = 'Library',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 1, border = 4, command = self.libraryInterface)
            self.btnLibrary_HomeInterface.grid(row = 0, column = 0)

            self.AuthorPhoto_HomeInterface = PhotoImage(file = (os.getcwd() + "/" + "Author@2x.png"))
            self.AuthorPotho_image_HomeInterface = self.AuthorPhoto_HomeInterface.subsample(1,1)
            self.btnAuthor_homeInterface = Button(self.mainFrame_HomeInterface, image = self.AuthorPotho_image_HomeInterface, text = 'Authors',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 1, border = 4, command = self.AuthorInterface)
            self.btnAuthor_homeInterface.grid(row = 1, column = 0, columnspan = 2)

            self.FavoritPhoto_HomeInterface = PhotoImage(file = (os.getcwd() + "/" + "Favorite@2x.png"))
            self.FavoritPhoto_image_HomeInterface = self.FavoritPhoto_HomeInterface.subsample(1,1)
            self.btnFavorit_homeInterface = Button(self.mainFrame_HomeInterface, image = self.FavoritPhoto_image_HomeInterface, text = 'Favorite',activebackground = ('white'), font = ('Comic Sans MS', 26,'bold'), borderless = 1, border = 4, command = self.FavoritInterface)
            self.btnFavorit_homeInterface.grid(row = 1, column = 1, columnspan = 2)

            self.AlbumPhoto_HomeInterface = PhotoImage(file = (os.getcwd() + "/" + "Album@2x.png"))
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

    def AlbumList_HomeInterface(self):  
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
        self.listRecentBook_HomeInterface.bind("<Double-Button-1>", self.openFeature_in_RecrntList)

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
            
        self.Library = True
        self.Author = False
        self.Favorite = False
        self.Album = False

        if self.Library == True:


            self.btnLibrary_leftFrame.config(background = '#3d84a8')
            self.btnAuthor_leftFrame.config(background = 'white')
            #self.btnCategory_leftFrame.config(background = 'white')
            self.btnAlbum_leftFrame.config(background = 'white')
            self.btnFavorit_leftFrame.config(background = 'white')

            if self.btnList == True:
                self.LibraryOnterface_in_List()
            if self.btnList == False:
                self.LibararyInterface_in_Grid()
            
    def LibraryOnterface_in_List(self):
        LibraryInterfaceaInList.LibraryInterfacea_in_List_Function(self.Main_Window ,self.rightFrame_mainWindow)
        
    def LibararyInterface_in_Grid(self):
        LibraryInterfaceInGird.Library_Interface_in_Gird_Function(self.rightFrame_mainWindow)

    def AuthorInterface(self):

        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()
        
        self.Library = False
        self.Author = True
        self.Favorite = False
        self.Album = False


            
        if self.Author == True:   
            self.btnAuthor_leftFrame.config(background = '#3d84a8')
            self.btnLibrary_leftFrame.config(background = 'white')
            #self.btnCategory_leftFrame.config(background = 'white')
            self.btnAlbum_leftFrame.config(background = 'white')
            self.btnFavorit_leftFrame.config(background = 'white')


            if self.btnList == True:
                self.AuthorInterface_in_list()

            if self.btnList == False:
                self.AuthorInterface_in_grid()

    def AuthorInterface_in_list(self):
        # Frame
        self.topFrame_AuthorInterface = Frame(self.rightFrame_mainWindow)
        self.topFrame_AuthorInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AuthorInterface.config(background = '#00EBFF')

        self.listFrame_AuthorInterface = Frame(self.rightFrame_mainWindow)
        self.listFrame_AuthorInterface.pack( pady = 10, padx = 5)

        self.leftFrame_AuthorInterface = Frame(self.listFrame_AuthorInterface)
        self.leftFrame_AuthorInterface.pack(side = 'left', padx = 5)

        self.mainFrame_AuthorInterface = Frame(self.listFrame_AuthorInterface)
        self.mainFrame_AuthorInterface.pack(fill = 'both', padx = 5)


                # Interface

        self.lblnameTap_AuthorInterface = Label(self.topFrame_AuthorInterface, text = 'Author', font = ('Times',20,'bold'), bg = '#00EBFF')
        self.lblnameTap_AuthorInterface.pack()

        self.AuthorNameList_AutorInterface()

        self.listBook_AuthorInterface = ttk.Treeview(self.mainFrame_AuthorInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '40')
        self.listBook_AuthorInterface.pack()
        self.listBook_AuthorInterface.bind("<Double-Button-1>", self.openFeature_inAuthorInterface)

        self.listBook_AuthorInterface.column('ID', width = '30')
        self.listBook_AuthorInterface.heading('ID', text = 'ID')

        self.listBook_AuthorInterface.column('Title', width = '190')
        self.listBook_AuthorInterface.heading('Title', text = 'Title')

        self.listBook_AuthorInterface.column('Author', width = '140')
        self.listBook_AuthorInterface.heading('Author', text = 'Author')

        self.listBook_AuthorInterface.column('Lenght', width = '65')
        self.listBook_AuthorInterface.heading('Lenght', text = 'Length')

        self.listBook_AuthorInterface.column('Last Readed', width = '160')
        self.listBook_AuthorInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_AuthorInterface.column('Date Added', width = '160')
        self.listBook_AuthorInterface.heading('Date Added', text = 'Date Added')

    def AuthorInterface_in_grid(self):
        pass

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
        
        self.Library = False
        self.Author = False
        self.Favorite = True
        self.Album = False

        if self.Favorite == True:
            self.btnAuthor_leftFrame.config(background = 'white')
            self.btnLibrary_leftFrame.config(background = 'white')
            #self.btnCategory_leftFrame.config(background = 'white')
            self.btnAlbum_leftFrame.config(background = 'white')
            self.btnFavorit_leftFrame.config(background = '#3d84a8')

            if self.btnList == True:
                self.FavoritInterface_in_list()
            if self.btnList == False:
                self.FavoritInterface_in_grid()
    
    def FavoritInterface_in_list(self):
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

        self.listBook_FavoriteInterface.column('Author', width = '210')
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

    def FavoritInterface_in_grid(self):
        pass

    def AlbumInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        self.Library = False
        self.Author = False
        self.Favorite = False
        self.Album = True



        if self.Album == True:
            self.btnLibrary_leftFrame.config(background = 'white')
            self.btnAuthor_leftFrame.config(background = 'white')
            #self.btnCategory_leftFrame.config(background = 'white')
            self.btnAlbum_leftFrame.config(background = '#3d84a8')
            self.btnFavorit_leftFrame.config(background = 'white')

            if self.btnList == True:
                self.AlbumInterface_in_list()
            if self.btnList == False:
                self.AlbumInterface_in_grid()

    def AlbumInterface_in_list(self):

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

        self.btnEditAlbum_AlbumInterface = Button(self.topFrame_AlbumInterface, text = 'Edit Album', border = 0, borderless = 10, width = 100, height = 30, command = EditAlbumFuntion.AlbumEditing)
        self.btnEditAlbum_AlbumInterface.pack(side = 'left')      

        self.lblnameTap_AlbumInterface = Label(self.topFrame_AlbumInterface, text = 'Album\t\t\t\t\t', font = ('Times',20,'bold'), bg = '#00EBFF')
        self.lblnameTap_AlbumInterface.pack(side = 'right')


        self.listBook_AlbumInterface = ttk.Treeview(self.mainFrame_AlbumInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = 40)
        self.listBook_AlbumInterface.pack()
        self.listBook_AlbumInterface.bind("<Double-Button-1>", self.OpenFunction_fromAlbumInterface)

        self.listBook_AlbumInterface.column('ID', width = '30')
        self.listBook_AlbumInterface.heading('ID', text = 'ID')

        self.listBook_AlbumInterface.column('Title', width = '190')
        self.listBook_AlbumInterface.heading('Title', text = 'Title')

        self.listBook_AlbumInterface.column('Author', width = '140')
        self.listBook_AlbumInterface.heading('Author', text = 'Author')

        self.listBook_AlbumInterface.column('Lenght', width = '75')
        self.listBook_AlbumInterface.heading('Lenght', text = 'Length')
    
        self.listBook_AlbumInterface.column('Last Readed', width = '160')
        self.listBook_AlbumInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_AlbumInterface.column('Date Added', width = '160')
        self.listBook_AlbumInterface.heading('Date Added', text = 'Date Added')
        
        self.listAllAlbum_AuthorInterface = ttk.Treeview(self.leftFrame_AlbumInterface, show = 'headings', column = ('All_Album'), height = 40)
        self.listAllAlbum_AuthorInterface.pack()

        self.listAllAlbum_AuthorInterface.column('All_Album', width = '200')
        self.listAllAlbum_AuthorInterface.heading('All_Album', text = 'All Album')
        self.listAllAlbum_AuthorInterface.bind("<Double-Button-1>", self.AlbumSelection_and_ShowData_in_DataList)


        self.ShwoDataIntoListAlbum()

    def AlbumInterface_in_grid(self):
        pass


#___________________________________________________________________________________________BACK-END__________________________________________________________________#


    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)

             

    def FileOpening_in_FavoriteInterface(self, event):
        time_Now = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d  %H:%M:%S"))
        ot = [time_Now]
        item = self.listBook_FavoriteInterface.selection()
        Name_Data = str(self.listBook_FavoriteInterface.item(item, "values")[1])
        ND = [Name_Data]

        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            tabelinDatabase = []
            self.c.execute('SELECT name from sqlite_master where type = "table"')
            for items in self.c.fetchall():
                tabelinDatabase.append(items[0])
            for Name_Table in (tabelinDatabase):
                if Name_Table != 'Album' and Name_Table != 'Authors':

                    TitleNameList = []
                    self.c.execute(f"SELECT * FROM [{Name_Table}]")
                    for TitleName in self.c.fetchall():
                        TitleNameList.append(TitleName[1])

                    if Name_Data in TitleNameList:
                        rowID = []
                        self.c.execute(f"SELECT rowid, * FROM [{Name_Table}] WHERE Title = (?)", ND)
                        for ID in self.c.fetchall():
                            rowID.append(ID[0])

                        self.c.execute(f"UPDATE [{Name_Table}] SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
                        self.conn.commit()

            self.conn.close()

        with self.change_dir('my_BookData/Data'):
                FileName = (os.getcwd() + "/" + Name_Data)
                subprocess.call(['open', FileName])
        self.Recent_Adding_Backend_fromFavorite(ND, ot)

    def Recent_Adding_Backend_fromFavorite(self, ND,  ot):
        with self.change_dir('my_BookData/Database'):
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

            rowID = []
            self.c.execute(f"SELECT rowid, * FROM Recent WHERE Title = (?)", ND)
            for ID in self.c.fetchall():
                rowID.append(ID[0])

            self.c.execute(f"UPDATE Recent SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
            self.conn.commit()

            self.conn.close()
        
        self.FavoritInterface()

    def OpenFunction_fromAlbumInterface(self, event):  
        time_Now = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d  %H:%M:%S"))
        ot = [time_Now]
        item = self.listBook_AlbumInterface.selection()
        Name_Data = str(self.listBook_AlbumInterface.item(item, "values")[1])
        ND = [Name_Data]

        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            tabelinDatabase = []
            self.c.execute('SELECT name from sqlite_master where type = "table"')
            for items in self.c.fetchall():
                tabelinDatabase.append(items[0])

            for Name_Table in (tabelinDatabase):
                if Name_Table != 'Album' and Name_Table != 'Authors':

                    TitleNameList = []
                    self.c.execute(f"SELECT * FROM [{Name_Table}]")
                    for TitleName in self.c.fetchall():
                        TitleNameList.append(TitleName[1])

                    if Name_Data in TitleNameList:
                        rowID = []
                        self.c.execute(f"SELECT rowid, * FROM [{Name_Table}] WHERE Title = (?)", ND)
                        for ID in self.c.fetchall():
                            rowID.append(ID[0])

                        self.c.execute(f"UPDATE [{Name_Table}] SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
                        self.conn.commit()

            self.conn.close()

        with self.change_dir('my_BookData/Data'):
            item = self.listBook_AlbumInterface.selection()
            Name_Data = str(self.listBook_AlbumInterface.item(item, "values")[1])

            FileName = (os.getcwd() + "/" + Name_Data)
            subprocess.call(['open', FileName])

        self.Recent_Adding_Backend_fromAlbum(ND, ot)

    def Recent_Adding_Backend_fromAlbum(self, ND, ot):
        with self.change_dir('my_BookData/Database'):
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

            rowID = []
            self.c.execute(f"SELECT rowid, * FROM Recent WHERE Title = (?)", ND)
            for ID in self.c.fetchall():
                rowID.append(ID[0])

            self.c.execute(f"UPDATE Recent SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
            self.conn.commit()

            self.conn.close()

    def Recent_Adding_to_list(self):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            for row in self.listRecentBook_HomeInterface.get_children():
                self.listRecentBook_HomeInterface.delete(row)

            self.c.execute("SELECT * FROM Recent")
            for RecentData in self.c.fetchall():
                self.listRecentBook_HomeInterface.insert("", 0, values = (RecentData[0], RecentData[1], RecentData[2], RecentData[3], RecentData[4], RecentData[5]))

            self.conn.close()

    def openFeature_in_RecrntList(self, event):
        time_Now = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d  %H:%M:%S"))
        ot = [time_Now]
        item = self.listRecentBook_HomeInterface.selection()
        Name_Data = str(self.listRecentBook_HomeInterface.item(item, "values")[1])
        ND = [Name_Data]

        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            tabelinDatabase = []
            self.c.execute('SELECT name from sqlite_master where type = "table"')
            for items in self.c.fetchall():
                tabelinDatabase.append(items[0])

            for Name_Table in (tabelinDatabase):
                if Name_Table != 'Album' and Name_Table != 'Authors':

                    TitleNameList = []
                    self.c.execute(f"SELECT * FROM [{Name_Table}]")
                    for TitleName in self.c.fetchall():
                        TitleNameList.append(TitleName[1])
                    
                    if Name_Data in TitleNameList:
                        rowID = []
                        self.c.execute(f"SELECT rowid, * FROM [{Name_Table}] WHERE Title = (?)", ND)
                        for ID in self.c.fetchall():
                            rowID.append(ID[0])

                        self.c.execute(f"UPDATE [{Name_Table}] SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
                        self.conn.commit()
                        

            self.conn.close()
        with self.change_dir('my_BookData/Data'):
            FileName = (os.getcwd() + "/" + Name_Data)
            subprocess.call(['open', FileName])
        self.Recent_Adding_Backend_fromRecent(ND, ot)

    def Recent_Adding_Backend_fromRecent(self, ND, ot):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.Recent_Selection = self.listRecentBook_HomeInterface.selection()
            self.Recent_Data_From_LibraryList = self.listRecentBook_HomeInterface.item(self.Recent_Selection,'values')

            self.RecentItem = [
                (
                self.Recent_Data_From_LibraryList[0], self.Recent_Data_From_LibraryList[1], self.Recent_Data_From_LibraryList[2], self.Recent_Data_From_LibraryList[3], self.Recent_Data_From_LibraryList[4], self.Recent_Data_From_LibraryList[5]
                )
            ]

            self.c.executemany("INSERT INTO Recent VALUES (?,?,?,?,?,?)", self.RecentItem)
            self.conn.commit()

            rowID = []
            self.c.execute(f"SELECT rowid, * FROM Recent WHERE Title = (?)", ND)
            for ID in self.c.fetchall():
                rowID.append(ID[0])

            self.c.execute(f"UPDATE Recent SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
            self.conn.commit()

            self.conn.close()
        self.homeInterfaceInterface()
        self.Recent_Adding_to_list()

    def FavoriteAdding_Function(self):
        FavoriteAdding.FavoriteAdding_from_Library()
        #self.FavoritInterface()

    def Favorite_Insrerting_Data_to_List(self):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()
    
            self.c.execute("SELECT * FROM Favorite")
            
            self.FavoriteItems = self.c.fetchall()
    
            for FavoriteItem in self.FavoriteItems:
                self.listBook_FavoriteInterface.insert("", END, values = (FavoriteItem[0], FavoriteItem[1], FavoriteItem[2], FavoriteItem[3], FavoriteItem[4], FavoriteItem[5]))
            self.conn.close()

    def DeleteData_From_FavoriteList(self):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.favoriteSelection = self.listBook_FavoriteInterface.selection()
            Name = [str(self.listBook_FavoriteInterface.item(self.favoriteSelection, 'values')[1])]

            self.c.execute("DELETE FROM Favorite WHERE Title = (?) " , Name[0:])
            self.conn.commit()
            self.conn.close()

        self.FavoritInterface()
    
    def ClearRecentListBook_in_Database(self):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("DELETE FROM Recent")
            self.conn.commit()
            self.conn.close()
        
        self.Recent_Adding_to_list()

    def ShwoDataIntoListAlbum(self):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("SELECT * FROM Album")
            
        for AlbumNameList in self.c.fetchall():
            self.listAllAlbum_AuthorInterface.insert("", END, values = (AlbumNameList))
        self.conn.close()

    def AlbumSelection_and_ShowData_in_DataList(self, event):
        with self.change_dir('my_BookData/Database'):
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
        with self.change_dir('my_BookData/Database'):
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
            self.conn.close()
        print(os.getcwd())
        self.AlbumInterface()

    def AddCategory_Into_CategoryNameList(self):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("SELECT * FROM Categories")
            for self.h in self.c.fetchall():
                self.tvListCategory_CategorInterface.insert("", END, values = (self.h))
            self.conn.close()

    def ShowCategories_in_DataList(self, event):
        with self.change_dir('my_BookData/Database'):
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
        with self.change_dir('my_BookData/Database'):
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
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("SELECT * FROM Authors")
            for h in self.c.fetchall():
                self.tvListName_HomeInterface.insert("", END, values = (h))

            self.conn.close()

    def OnDoubleClick_Author(self, event):
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            for row in self.listBook_AuthorInterface.get_children():
                self.listBook_AuthorInterface.delete(row)

            item = self.tvListName_AuthorInterface.selection()

            AuthorsNameItem = self.tvListName_AuthorInterface.item(item ,"values")[0]

            self.c.execute(f"SELECT * FROM [{AuthorsNameItem}]")
            for AuthorData_into_AuthorsNameList in self.c.fetchall():
                self.listBook_AuthorInterface.insert("", END, values = (AuthorData_into_AuthorsNameList[0], AuthorData_into_AuthorsNameList[1], AuthorData_into_AuthorsNameList[2], AuthorData_into_AuthorsNameList[3], AuthorData_into_AuthorsNameList[4], AuthorData_into_AuthorsNameList[5]))
            self.conn.close()
    
    def openFeature_inAuthorInterface(self, event):
        time_Now = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d  %H:%M:%S"))
        ot = [time_Now]
        item = self.listBook_AuthorInterface.selection()
        Name_Data = str(self.listBook_AuthorInterface.item(item, "values")[1])
        ND = [Name_Data]

        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            tabelinDatabase = []
            self.c.execute('SELECT name from sqlite_master where type = "table"')
            for items in self.c.fetchall():
                tabelinDatabase.append(items[0])

            for Name_Table in (tabelinDatabase):
                if Name_Table != 'Album' and Name_Table != 'Authors':

                    TitleNameList = []
                    self.c.execute(f"SELECT * FROM [{Name_Table}]")
                    for TitleName in self.c.fetchall():
                        TitleNameList.append(TitleName[1])

                    if Name_Data in TitleNameList:
                        rowID = []
                        self.c.execute(f"SELECT rowid, * FROM [{Name_Table}] WHERE Title = (?)", ND)
                        for ID in self.c.fetchall():
                            rowID.append(ID[0])

                        self.c.execute(f"UPDATE [{Name_Table}] SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
                        self.conn.commit()

        with self.change_dir('my_BookData/Data'):
            FileName = (os.getcwd() + "/" + Name_Data)
            subprocess.call(['open', FileName])
        self.Recent_Adding_Backend_fromAuthors_Inyterface(ND, ot)

    def Recent_Adding_Backend_fromAuthors_Inyterface(self, ND, ot):
        with self.change_dir('my_BookData/Database'):
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

            rowID = []
            self.c.execute(f"SELECT rowid, * FROM Recent WHERE Title = (?)", ND)
            for ID in self.c.fetchall():
                rowID.append(ID[0])

            self.c.execute(f"UPDATE Recent SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
            self.conn.commit()

            self.conn.close()    
            
    def ConfiguringListandGrid(self):
        
        
        if self.btnList == False:
            self.btnListAndGrid_mainrightFrame.config(text = '􀋲')
            self.btnListAndGrid_mainrightFrame.config(bg = 'lime')
            self.btnList = True
        
            if self.Library == True:
                self.libraryInterface()
            if self.Author == True:
                self.AuthorInterface()
            if self.Favorite == True:
                self.FavoritInterface()
            if self.Album == True:
                self.AlbumInterface()

            #self.libraryInterface()
            #self.AuthorInterface()
            #self.FavoritInterface()
            #self.AlbumInterface()

            
            
        else:    
            self.btnListAndGrid_mainrightFrame.config(text = '􀇴')
            self.btnListAndGrid_mainrightFrame.config(bg = 'gray')
            self.btnList = False
            
            if self.Library == True:
                self.libraryInterface()
            if self.Author == True:
                self.AuthorInterface()
            if self.Favorite == True:
                self.FavoritInterface()
            if self.Album == True:
                self.AlbumInterface()
                
            #self.libraryInterface()
            #self.AuthorInterface()
            #self.FavoritInterface()
            #self.AlbumInterface()
            
            
            
            

if __name__ == "__main__":
    MainfileApplication() 
