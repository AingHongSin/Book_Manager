import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import os
from PIL import ImageTk, Image
import tkinter.filedialog
from PyPDF2 import PdfFileReader
from collections import OrderedDict
import datetime




class MainfileApplication():

    def __init__(self):

        

        self.Main_Window = tk.Tk()
        self.Main_Window.title("My_BooK")
        self.Main_Window.geometry("1100x500+300+200")
        #self.Main_Window.resizable(False, False)

        os.chdir('/Users/macbook/Documents/Project/Book_Manager')

        self.disBookList = {}
        self.disBookList["Title"] = self.Title_List = []
        self.disBookList["Author"] = self.Author_List = []
        self.disBookList["Category"] = self.Category_list = []
        self.disBookList["Length"] = self.Length_list = []
        
        self.Amount_Book = 1
        self.Amount_Data = 1

        # Variable
                # Author Tuple
        self.btn_All_AuthorName = ['Author1', 'Author2', 'Author3']
        self.Author_index = 0

                # Category Tuple
        self.btn_All_CategoryName = ['Category1', 'Category2', 'Category3']
        self.Category_index = 0

                # Album Tuple

        self.Add_Data_Into_App()


        # Frame

        self.leftFrame_mainWindow = tk.Frame(self.Main_Window)
        self.leftFrame_mainWindow.pack(side = 'left', fill = 'y')
        self.leftFrame_mainWindow.config(background = '#a6a6a6')

        self.topFrame_mainWindow = tk.Frame(self.Main_Window )
        self.topFrame_mainWindow.pack(side = 'top', fill = 'x')
        self.topFrame_mainWindow.config(background = '#666666')
        
        self.rightFrame_mainWindow = tk.Frame(self.Main_Window)
        self.rightFrame_mainWindow.pack(fill = 'both')
        
        # InterFace 
                            # TopFrame
        self.lblTitle_TopFrame = tk.Label(self.topFrame_mainWindow, text = 'My BooK', font = ('defule',28,'bold'), bg = '#666666')
        self.lblTitle_TopFrame.pack()


                            # LeftFrame
        self.homephoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/home.png")
        self.homePhoto_image = self.homephoto.subsample(10,10)

        self.btnHome_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.homePhoto_image, width = '140' , command = self.homeInterfaceInterface)
        self.btnHome_leftFrame.pack()
        #self.btnHome_leftFrame.configure({"bg": "white", "activebackground": "white"})


        self.btnLibrary_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '📚\tLibrary', height = '2', width = '15', command = self.libraryInterface)
        self.btnLibrary_leftFrame.pack()

        self.btnAuthor_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '👨‍💼\tAuthor', height = '2', width = '15', command = self.AuthorInterface)
        self.btnAuthor_leftFrame.pack()
        
        self.btnCategory_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '🗄\tCategory', height = '2', width = '15', command = self.CategoryInterface)
        self.btnCategory_leftFrame.pack()

        self.btnFavorit_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '🤍\tFevorite', height = '2', width = '15', command = self.FavoritInterface)
        self.btnFavorit_leftFrame.pack()

        self.btnAlbum_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '🗃\tAlbum', height = '2', width = '15', command = self.AlbumInterface)
        self.btnAlbum_leftFrame.pack()

        self.btnExit_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '❌\tExit', height = '2', width = '15', command = self.Main_Window.destroy)
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
        self.LibraryPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Library2.png")
        self.LibraryPotho_image = self.LibraryPhoto.subsample(10,10)
        self.btnLibrary_HomeInterface = tk.Button(self.mainFrame_HomeInterface, image = ( self.LibraryPotho_image), text = '\t\tLibrary     ', compound = 'left', font = ('default',15), command = self.libraryInterface)
        self.btnLibrary_HomeInterface.pack()

        self.AuthorPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Author1.png")
        self.AuthorPotho_image = self.AuthorPhoto.subsample(11,11)
        self.btnAuthor_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.AuthorPotho_image, text = '\t\t\tAuthor\t', compound = 'left', font = ('default',15), command = self.AuthorInterface)
        self.btnAuthor_homeInterface.pack()

        self.CategoriesPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Categories.png")
        self.CategoriesPotho_image = self.CategoriesPhoto.subsample(10,10)
        self.btnCategory_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.CategoriesPotho_image, text = '\t\t\t\tCategoriest    ', compound = 'left', font = ('default',15), command = self.CategoryInterface)
        self.btnCategory_homeInterface.pack()

        self.FavoritPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Favorit.png")
        self.FavoritPhoto_image = self.FavoritPhoto.subsample(18,18)
        self.btnFavorit_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.FavoritPhoto_image, text = '\t\t\t\t\t  Favorite\t', compound = 'left', font = ('default',15), command = self.FavoritInterface)
        self.btnFavorit_homeInterface.pack()

        self.AlbumPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Album.png")
        self.AlbumPotho_image = self.AlbumPhoto.subsample(20,20)
        self.btnAlbum_homeInterfac = tk.Button(self.mainFrame_HomeInterface, image = self.AlbumPotho_image, text = '\t\t\t\t\t\tAlbum\t', compound = 'left', font = ('default',15), command = self.AlbumInterface)
        self.btnAlbum_homeInterfac.pack()



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

        self.btnDeleteBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Edit', width = '10', height ='2')
        self.btnDeleteBook_LibraryInterface.pack(side = 'left')   

        self.btnBookDetail_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Detail', width = '10', height = '2')
        self.btnBookDetail_LibraryInterface.pack(side = 'left')   

        self.btnFavoritAdding_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Favorit Adding', width = '10', height = '2', command = self.FavoritAdding)
        self.btnFavoritAdding_LibraryInterface.pack(side = 'left')

                            # main Interface
        self.listBook_libraryInterface = tk.ttk.Treeview(self.mainFrame_libraryInterface, column = ('Title', 'Author', 'Category', 'Lenght', 'Favorit' """, 'Last Readed', 'Date Added'"""), show = 'headings', height = '30')
        self.listBook_libraryInterface.pack(padx = '10', pady = '5')


        self.listBook_libraryInterface.column('Title', width = '300')
        self.listBook_libraryInterface.heading('Title', text = 'Title')

        self.listBook_libraryInterface.column('Author', width = '200')
        self.listBook_libraryInterface.heading('Author', text = 'Author')

        self.listBook_libraryInterface.column('Category', width = '150')
        self.listBook_libraryInterface.heading('Category', text = 'Category')

        #self.listBook_libraryInterface.column('Last Readed', width = '100')
        #self.listBook_libraryInterface.heading('Last Readed', text = 'Last Readed')
    
        #self.listBook_libraryInterface.column('Date Added', width = '100')
        #self.listBook_libraryInterface.heading('Date Added', text = 'Date Added')
        
        self.listBook_libraryInterface.column('Lenght', width = '130')
        self.listBook_libraryInterface.heading('Lenght', text = 'Length')
        
        #self.listBook_libraryInterface.column('Favorit', width = '80')
        #self.listBook_libraryInterface.heading('Favorit', text = 'Favorite')

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
        self.leftFrame_AuthorInterface.configure(background = '#c8c8c8')

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

    def Backenf_of_AuthorInterface(self):

        self.tvListName = tk.ttk.Treeview(self.leftFrame_AuthorInterface, column = ('Author_Name'), show = 'headings', height = '80')
        self.tvListName.pack()

        self.tvListName.column('Author_Name', width = '130')
        self.tvListName.heading('Author_Name', text = 'All Authors')

        self.AddAuthorlist_into_AuthorInterface()

    def OnDoubleClick_Author(self, event):

        item = self.tvListName.selection()
        print("This is ", str(self.tvListName.item(item ,"values")[0]))

    def ListName_for_Each_Author(self):

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

        self.listBook_CategoryInterface = tk.ttk.Treeview(self.mainFrame_CategoryInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_CategoryInterface.pack(padx = '10', pady = '5')

        self.listBook_CategoryInterface.column(1, width = '150')
        self.listBook_CategoryInterface.heading(1, text = 'Title')

        self.listBook_CategoryInterface.column(2, width = '150')
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

        self.tvListCategory = tk.ttk.Treeview(self.leftFrame_CategoryInterface, column = ('Category_Name'), show = 'headings', height = '80')
        self.tvListCategory.pack()

        self.tvListCategory.column('Category_Name', width = '130')
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

        self.btnDeleteBook_FavoriteInterface = tk.Button(self.topFrame_FavoriteInterface, text = 'Delete', width = '10', height ='2')
        self.btnDeleteBook_FavoriteInterface.pack(side = 'left')      


                            # main Interface
        self.listBook_FavoriteInterface = tk.ttk.Treeview(self.mainFrame_FevoriteInterface, column = ('Title', 'Author', 'Category', 'Last Readed', 'Date Added', 'Size', 'Favorit'), show = 'headings', height = '30')
        self.listBook_FavoriteInterface.pack(padx = '10', pady = '5')

        self.listBook_FavoriteInterface.column('Title', width = '200')
        self.listBook_FavoriteInterface.heading('Title', text = 'Title')

        self.listBook_FavoriteInterface.column('Author', width = '200')
        self.listBook_FavoriteInterface.heading('Author', text = 'Authot')

        self.listBook_FavoriteInterface.column('Category', width = '150')
        self.listBook_FavoriteInterface.heading('Category', text = 'Category')

        self.listBook_FavoriteInterface.column('Last Readed', width = '100')
        self.listBook_FavoriteInterface.heading('Last Readed', text = 'Last Readed')
        
        self.listBook_FavoriteInterface.column('Date Added', width = '100')
        self.listBook_FavoriteInterface.heading('Date Added', text = 'Date Added')
        
        self.listBook_FavoriteInterface.column('Size', width = '80')
        self.listBook_FavoriteInterface.heading('Size', text = 'Size')
        
        self.listBook_FavoriteInterface.column('Favorit', width = '80')
        self.listBook_FavoriteInterface.heading('Favorit', text = 'Favorite')
        
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
        self.btnAddBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Add Album', width = '10',height = '2')
        self.btnAddBook_AlbumInterface.pack(side = 'left')

        self.btnDeleteBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Delete Album', width = '10', height ='2')
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.btnDeleteBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Edit Album', width = '10', height ='2')
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.lblnameTap_AlbumInterface = tk.Label(self.topFrame_AlbumInterface, text = 'Album', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_AlbumInterface.pack(side = 'right')

        self.listBook_AlbumInterface = tk.ttk.Treeview(self.mainFrame_AlbumInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_AlbumInterface.pack(padx = '10', pady = '5')

        self.listBook_AlbumInterface.column(1, width = '150')
        self.listBook_AlbumInterface.heading(1, text = 'Title')

        self.listBook_AlbumInterface.column(2, width = '150')
        self.listBook_AlbumInterface.heading(2, text = 'Authot')

        self.listBook_AlbumInterface.column(3, width = '150')
        self.listBook_AlbumInterface.heading(3, text = 'Category')

        self.listBook_AlbumInterface.column(4, width = '100')
        self.listBook_AlbumInterface.heading(4, text = 'Last Readed')
        
        self.listBook_AlbumInterface.column(5, width = '100')
        self.listBook_AlbumInterface.heading(5, text = 'Date Added')
        
        self.listBook_AlbumInterface.column(6, width = '80')
        self.listBook_AlbumInterface.heading(6, text = 'Size')
        
        self.listBook_AlbumInterface.column(7, width = '80')
        self.listBook_AlbumInterface.heading(7, text = 'Favorite')

#_______________________________________________________________________BACK-END_____________________________________________________________________________________________#

    def Add_Data_Into_App(self):
    
        os.chdir('/Users/macbook/Documents/Project/Book_Manager/Data')

        self.d = os.listdir()

        for row in self.d:
            if row != '.DS_Store':
                self.Title_List.append(str(row))
        
                pdf_path = str(row)
                with open(pdf_path, 'rb') as f:
                    self.pdf = PdfFileReader(f)
                    self.information = self.pdf.getDocumentInfo()
                    self.number_of_pages = self.pdf.getNumPages()
                
                self.Author_List.append(str(self.information.author))
                self.Category_list.append(str(None))
                self.Length_list.append(str(self.number_of_pages))

                print("Author :", self.disBookList['Author'])
                print("Title :", self.disBookList['Title'])
                print("All Amount data :", len(self.disBookList['Title'][0:]))
    
    def library_Data_Adding(self):
        print(self.disBookList)
        for a in range(len(self.disBookList["Title"])):
            self.listBook_libraryInterface.insert("", tk.END, values = (self.disBookList["Title"][a], self.disBookList["Author"][a], self.disBookList["Category"][a], (self.disBookList["Length"][a] + "\tpages")))
            self.listBook_libraryInterface.bind("<Double-Button-1>", self.openFeature)

    def openFeature(self, event):
        item = self.listBook_libraryInterface.selection()
        print(self.listBook_libraryInterface.item(item, "values"), 'Open at', datetime.datetime.now().astimezone().strftime("%Y-%m-%d,  %H:%M:%S"))

    
    def AddAuthorlist_into_AuthorInterface(self):
        if self.disBookList["Author"] == self.Author_List:
            for a in range(len(self.disBookList["Author"])):
                self.tvListName.insert("", tk.END, values = ((self.disBookList["Author"][a:])))
                self.tvListName.bind("<Double-Button-1>", self.AuthorList)

    def AuthorList(self, event):
        item = self.tvListName.selection()
        print(self.tvListName.item(item, "values")[0])
    
    def FavoritAdding(self):

        Dataitem = self.listBook_libraryInterface.focus()
        print(self.listBook_libraryInterface.item(Dataitem))
        if Dataitem:
             print(self.listBook_libraryInterface.item(Dataitem, "values"), 'Open at', datetime.datetime.now().astimezone().strftime("%Y-%m-%d,  %H:%M:%S"))


if __name__ == "__main__":
    MainfileApplication() 
