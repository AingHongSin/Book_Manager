import os
import sqlite3
import subprocess
import datetime
import tkinter.messagebox
import tkinter.dialog
import shutil

import DetailFunction
import ExtractMetadaFromPDF

from tkinter import *
from tkinter import ttk
from tkmacosx import Button 
from PyPDF2 import PdfFileReader
from contextlib import contextmanager

class LibraryInterfacea_in_List_Function():

    def __init__(self, Main_window, rightFrame_mainWindow):
        
        self.Main_window = Main_window
        
        
        
        # Frame
        self.topFrame_LibraryInterface = Frame(rightFrame_mainWindow)
        self.topFrame_LibraryInterface.pack(side = 'top', fill = 'x')
        self.topFrame_LibraryInterface.config(background = '#00EBFF')

        self.mainFrame_libraryInterface = Frame(rightFrame_mainWindow)
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

        self.btnFavoritAdding_LibraryInterface = Button(self.topFrame_LibraryInterface, text = 'Favorit Adding', border = 0, borderless = 10, width = 130, height = 30, command = self.FavoritAddingBackend_from_LibraryInterface)
        self.btnFavoritAdding_LibraryInterface.pack(side = 'left')

                            # main Interface
        self.listBook_libraryInterface = ttk.Treeview(self.mainFrame_libraryInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '40')
        self.listBook_libraryInterface.pack(padx = '10', pady = '10')
        self.listBook_libraryInterface.bind("<Double-Button-1>", self.openFeature)

        self.listBook_libraryInterface.column('ID', width = '40')
        self.listBook_libraryInterface.heading('ID', text = 'ID')

        self.listBook_libraryInterface.column('Title', width = '250')
        self.listBook_libraryInterface.heading('Title', text = 'Title')

        self.listBook_libraryInterface.column('Author', width = '210')
        self.listBook_libraryInterface.heading('Author', text = 'Author')

        self.listBook_libraryInterface.column('Lenght', width = '120')
        self.listBook_libraryInterface.heading('Lenght', text = 'Length')

        self.listBook_libraryInterface.column('Last Readed', width = '170')
        self.listBook_libraryInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_libraryInterface.column('Date Added', width = '170')
        self.listBook_libraryInterface.heading('Date Added', text = 'Date Added')

        self.library_Data_Adding()

    def library_Data_Adding(self):
        
        for widget in self.listBook_libraryInterface.winfo_children():
            widget.destroy()
        with self.change_dir('my_BookData/Database'):

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
        self.listBook_libraryInterface.selection_toggle(self.listBook_libraryInterface.focus())


    def openFeature(self, Event):
        time_Now = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d  %H:%M:%S"))
        ot = [time_Now]
        item = self.listBook_libraryInterface.focus()

        try:
            Name_Data = str(self.listBook_libraryInterface.item(item, "values")[1])
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
            self.Recent_Adding_Backend_fromLibrary(ND, ot)
        except IndexError:
            print('', end='')

    def Recent_Adding_Backend_fromLibrary(self, ND, ot):
        with self.change_dir('my_BookData/Database'):
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
            rowID = []
            self.c.execute(f"SELECT rowid, * FROM Recent WHERE Title = (?)", ND)
            for ID in self.c.fetchall():
                rowID.append(ID[0])
            self.c.execute(f"UPDATE Recent SET Last_Readed  = (?) WHERE rowID = {rowID[0]}", ot)
            self.conn.commit()
            self.conn.close()
        
        
    def DeleteFile_FromData(self):

        with self.change_dir('my_BookData/splitting'):
            self.SelectionItemfromList = self.listBook_libraryInterface.selection()
            self.NameSelectionItem = self.listBook_libraryInterface.item(self.SelectionItemfromList, 'values')[1]
            os.remove(f"{self.NameSelectionItem}")
        with self.change_dir('my_BookData/Img'):
            try:
                self.SelectionItemfromList = self.listBook_libraryInterface.selection()
                self.NameSelectionItem = self.listBook_libraryInterface.item(self.SelectionItemfromList, 'values')[1]
                self.IDSelectionItem = self.listBook_libraryInterface.item(self.SelectionItemfromList, 'values')[0]
                os.remove(os.getcwd() + "/" + self.NameSelectionItem + ".png" )                
            except IndexError as e:
                tkinter.messagebox.showwarning('Warning', 'Please Choose one file.')
        with self.change_dir('my_BookData/Data'):
            try:
                self.SelectionItemfromList = self.listBook_libraryInterface.selection()
                self.NameSelectionItem = self.listBook_libraryInterface.item(self.SelectionItemfromList, 'values')[1]
                self.IDSelectionItem = self.listBook_libraryInterface.item(self.SelectionItemfromList, 'values')[0]
                os.remove(f"{self.NameSelectionItem}")
                os.chdir(os.path.dirname(os.getcwd()))
                self.deleteDatafromDatabase(self.NameSelectionItem)     
            except IndexError as e:
                tkinter.messagebox.showwarning('Warning', 'Please Choose one file.')

    def FavoritAddingBackend_from_LibraryInterface(self):
        try:
            with self.change_dir('my_BookData/Database'):
                self.conn = sqlite3.connect('Libraries.db')
                self.c = self.conn.cursor()
                favoriteList = []
                Dataitem = self.listBook_libraryInterface.selection()
                FavoriteData = (self.listBook_libraryInterface.item(Dataitem, "values"))
                FD = str(FavoriteData[1])
                self.c.execute("SELECT * FROM Favorite")
                for f in self.c.fetchall():
                    favoriteList.append(f[1])
                if FD in favoriteList:
                    tkinter.messagebox.showerror('Error', 'This file has been added. ')
                else:
                    if FD != favoriteList:
                        FavoriteManyData = [
                                (
                                FavoriteData[0], FavoriteData[1], FavoriteData[2], FavoriteData[3], FavoriteData[4], FavoriteData[5]
                                )
                            ]
                        self.c.executemany("INSERT INTO Favorite VALUES (?,?,?,?,?,?)", FavoriteManyData)
                        self.conn.commit()
                        self.conn.close()
        except IndexError as e :
            tkinter.messagebox.showwarning('Warning', 'Please choose one book for add into Favorite')


    def openFileDailog_for_AddFile(self):
        with self.change_dir('my_BookData/Data'):
            self.Main_window.filename = tkinter.filedialog.askopenfilename(initialdir = "/Users/privateman/Documents", title = "Select a pdf file", filetypes = (("pdf files", "*.pdf"),("all files", "*.*")) )

            self.orginalpath = self.Main_window.filename
            self.destinationPath = os.getcwd()

            pdf_path = self.orginalpath
            try:
                with open(pdf_path, 'rb') as f:
                    self.pdf = PdfFileReader(f)
                    if self.pdf.isEncrypted:
                        tkinter.messagebox.showerror('Error', "This file has not support")
                    else:
                        if self.orginalpath != '':
                            shutil.copy(self.orginalpath, self.destinationPath)
            except FileNotFoundError:
                print("", end='')

        ExtractMetadaFromPDF.Extract_Metada_From_PDF()
        #self.AuthorFunction()


    def DetailFunction_LibraryInterface(self):
        try:
            selectItem = self.listBook_libraryInterface.selection()
            Name = self.listBook_libraryInterface.item(selectItem, 'values')[1]

            with self.change_dir('my_BookData/Data'):

                pdf_path = str(Name)

                with open(pdf_path, 'rb') as f:
                    pdf = PdfFileReader(f)
                    information = pdf.getDocumentInfo()
                    number_of_pages = pdf.getNumPages()
                    p = pdf.getPage(0)


                Title =  (information.title)
                Author =  (information.author)
                Creator =  (information.creator)
                Producer =  (information.producer)
                Subject =  (information.subject)
                Number_of_pages =  (number_of_pages)

                w_in_user_space_units = p.mediaBox.getWidth()
                h_in_user_space_units = p.mediaBox.getHeight()      

                # 1 user space unit is 1/72 inch
                # 1/72 inch ~ 0.352 millimeters     

                w = int(float(p.mediaBox.getWidth()) * 0.352)
                h = int(float(p.mediaBox.getHeight()) * 0.352)

                page_size = (w,'mm' ,'x',h,'mm')

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

            DetailFunction.DetailFunction(Name, Title, Author, Creator, Producer, Subject, Number_of_pages, page_size)

        except IndexError as e :
            tkinter.messagebox.showwarning('Warning', 'Please choose one book for show Detail')


    def deleteDatafromDatabase(self, IDSelection):
        IDSelectionItem = str(IDSelection)
        tabelinDatabase = []

        with self.change_dir('Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute('SELECT name from sqlite_master where type = "table"')
            for items in self.c.fetchall():
                tabelinDatabase.append(items[0])

            for t in range(len(tabelinDatabase)):
                o = str(tabelinDatabase[t])

                tabelinDatabase[t] = []
                self.c.execute(f"SELECT * FROM [{o}]")
                for k in self.c.fetchall():
                    tabelinDatabase[t].append(k[1])


                if IDSelectionItem in tabelinDatabase[t]:
                    dt = []
                    ID  = [IDSelectionItem]
                    self.c.execute(f"DELETE FROM [{o}] WHERE Title = (?)", ID[0:] )
                    self.conn.commit()

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

            self.conn.commit()
            self.conn.close() 

        print(os.getcwd())
        os.chdir(os.path.dirname(os.getcwd()))




    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)