import os
import sqlite3
import AddDataintoAlbum
import tkinter.messagebox
import RenamAlbumName
from tkinter import *
from tkinter import ttk
from tkmacosx import Button
from contextlib import contextmanager


class AlbumEditing():
    def __init__(self):
        self.EditingAlbum_TopLevel = Toplevel()
        self.EditingAlbum_TopLevel.title("Album Edting")
        self.EditingAlbum_TopLevel.geometry("730x330+500+250")

        # Frame
        self.TopFrame = Frame(self.EditingAlbum_TopLevel, bg = '#00EBFF')
        self.TopFrame.pack(fill = 'x', side = 'top')

        self.MainFrame = Frame(self.EditingAlbum_TopLevel)
        self.MainFrame.pack(fill = 'x')

        self.TopFrame_MainFrame = Frame(self.MainFrame)
        self.TopFrame_MainFrame.pack(fill = 'x')
        
        self.MainFrame_MainFrame = LabelFrame(self.MainFrame)
        self.MainFrame_MainFrame.pack(fill = 'x')
        
        self.ButtomFrame = Frame(self.EditingAlbum_TopLevel, bg = '#00EBFF')
        self.ButtomFrame.pack(fill = 'x', side = 'bottom')

        # Interface 
        self.lblTitle = Label(self.TopFrame, text = 'Album Modify', bg = '#00EBFF', font = ('Times', 21, 'bold'))
        self.lblTitle.pack()

        ItemList = ['']

        #self.sptTitle = ttk.Separator(self.TopFrame)
        #self.sptTitle.pack(fill = 'x', padx = 10)

        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("SELECT * FROM Album")
            for Items in self.c.fetchall():
                ItemList.append(Items[0])
            self.conn.close()

        style = ttk.Style()
        style.configure('TCombobox', borderless = 10, border = 10)

        self.lblNameAlbum = Label(self.TopFrame_MainFrame, text = 'All Album Name :')
        self.lblNameAlbum.pack(side = 'left')

        self.spinAlbumName = ttk.Combobox(self.TopFrame_MainFrame, style = 'TCombobox', values = ItemList , height = 20)
        self.spinAlbumName.pack(side = 'left', pady = 5)
        self.spinAlbumName.bind('<<ComboboxSelected>>', self.AlbumName)

        self.btnRename = Button(self.TopFrame_MainFrame, text = 'Rename', borderless = 10, command = self.RenameFucniotn)
        self.btnRename.pack(side = 'right', pady = 5)

        self.btnAdd = Button(self.TopFrame_MainFrame, text = 'Add', borderless = 10, command = self.AddingFunciton)
        self.btnAdd.pack(side = 'right', pady = 5)

        self.btnDelete = Button(self.TopFrame_MainFrame, text = 'Delete', borderless = 10, command = self.DeleteDataFromAlbumList)
        self.btnDelete.pack(side = 'right', pady = 5)

        self.listBook()

        self.btnDone = Button(self.ButtomFrame, text = 'Done', height = 30, border = 0, borderless = 4, command = self.EditingAlbum_TopLevel.destroy)
        self.btnDone.pack(side = 'right', padx = 5, pady = 5)

        self.EditingAlbum_TopLevel.mainloop()   

    def RenameFucniotn(self):
        Album_Name = self.spinAlbumName.get()
        if Album_Name != '':
            RenamAlbumName.RenameTable_and_AlbumData(Album_Name)     
        
    def AlbumName(self, event):
        for row in self.listBook_Interface.get_children():
            self.listBook_Interface.delete(row)

        if self.spinAlbumName.get() != '':
            print(self.spinAlbumName.get())
            AlbumList = self.spinAlbumName.get()

            with self.change_dir('my_BookData/Database'):
                self.conn = sqlite3.connect('Libraries.db')
                self.c = self.conn.cursor()

                self.c.execute(f"SELECT * FROM [{AlbumList}]")
            for Items in self.c.fetchall():
                self.listBook_Interface.insert("", END, values = (Items[0], Items[1], Items[2], Items[3], Items[4], Items[5]))
                
            self.conn.close()

    def listBook(self):

        self.listBook_Interface = ttk.Treeview(self.MainFrame_MainFrame, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '10')
        self.listBook_Interface.pack(padx = '10', pady = '10')

        self.listBook_Interface.column('ID', width = '30')
        self.listBook_Interface.heading('ID', text = 'ID')

        self.listBook_Interface.column('Title', width = '180')
        self.listBook_Interface.heading('Title', text = 'Title')

        self.listBook_Interface.column('Author', width = '120')
        self.listBook_Interface.heading('Author', text = 'Author')

        self.listBook_Interface.column('Lenght', width = '50')
        self.listBook_Interface.heading('Lenght', text = 'Length')

        self.listBook_Interface.column('Last Readed', width = '160')
        self.listBook_Interface.heading('Last Readed', text = 'Last Readed')

        self.listBook_Interface.column('Date Added', width = '160')
        self.listBook_Interface.heading('Date Added', text = 'Date Added')

    def DeleteDataFromAlbumList(self):
        try:
            Select = self.listBook_Interface.selection()
            Name = str(self.listBook_Interface.item(Select, 'values')[1])
            p = [Name]
            print(p[0])

            AlbumNamne = self.spinAlbumName.get()
            t = [AlbumNamne]
            with self.change_dir('my_BookData/Database'):
                self.conn = sqlite3.connect('Libraries.db')
                self.c = self.conn.cursor()

                self.c.execute(f"DELETE FROM [{AlbumNamne}] WHERE Title = (?)", p)
                self.conn.commit()

                dt = []
                self.c.execute(f"SELECT * FROM [{AlbumNamne}]")
                for y in self.c.fetchall():
                    dt.append(y[0])
                if dt == []:
                    self.c.execute(f"DROP TABLE [{AlbumNamne}]")
                    self.conn.commit()

                    self.c.execute("DELETE FROM Album WHERE Album_NameList = (?)", t )
                    self.conn.commit()

                    self.Reface_Interface()

            self.conn.close()
        except IndexError :
            tkinter.messagebox.showwarning('Warning', 'If you want to delete any file Please selelct any file first.')
    
    def Reface_Interface(self):
        os.chdir(os.path.dirname(os.getcwd()))
        self.EditingAlbum_TopLevel.destroy()
        self.__init__()

    def Recall_Function(self):
        self.listBook()

    def AddingFunciton(self):
        AlbumNamne = self.spinAlbumName.get()
        if AlbumNamne != '':
            AddDataintoAlbum.Adding_from_Library_into_Adlbum(AlbumNamne)
            #self.EditingAlbum_TopLevel.destroy()
            #self.__init__()


    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)

#if __name__ == "__main__":
#    AlbumEditing()