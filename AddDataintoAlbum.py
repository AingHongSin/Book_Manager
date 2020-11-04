import os
import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkmacosx import Button
from contextlib import contextmanager

class Adding_from_Library_into_Adlbum():
    def __init__(self, AlbumNamne):
        
        self.AlbumNamne = AlbumNamne

        self.AddData_into_List = Toplevel()
        self.AddData_into_List.title('Album Adding Data')
        self.AddData_into_List.geometry('730x330+500+250')
        
        # Frame
        self.topFrame = Frame(self.AddData_into_List, bg = '#00ebff')
        self.topFrame.pack(fill = 'x', side = 'top')

        self.SecondFrame = Frame(self.AddData_into_List)
        self.SecondFrame.pack(fill = 'x')

        self.mainFrame = LabelFrame(self.AddData_into_List)
        self.mainFrame.pack()
        
        self.BottomFrame = Frame(self.AddData_into_List, bg = '#00ebff')
        self.BottomFrame.pack(side = 'bottom', fill = 'x')


        # Interface
        self.lblTitle = Label(self.topFrame, text = 'Album Adding Data', bg = '#00EBFF', font = ('Times', 21, 'bold'))
        self.lblTitle.pack()

        self.btnAdd  = Button(self.SecondFrame, text = 'Add', borderless = 4, command = self.DataAdding)
        self.btnAdd.pack(side = 'right', pady = 5)

        self.listBook_Interface = ttk.Treeview(self.mainFrame, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '10')
        self.listBook_Interface.pack(padx = 10, pady = 10)

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

        self.btnDone = Button(self.BottomFrame, text = 'Done', borderless = 4, height = 30, command = self.DoneFunction)
        self.btnDone.pack(side = 'right', padx = 5, pady = 5)


        with self.change_dir('my_BookData/Database'):   
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("SELECT * FROM Data_list ")
            self.items = self.c.fetchall()
            for item in self.items:
                if item[2] == None:
                    self.listBook_Interface.insert("", END, values = (item[0], item[1], 'Unknown Author', item[3],  item[4], item[5] ))
                else: 
                    self.listBook_Interface.insert("", END, values = (item[0], item[1], item[2], item[3],  item[4], item[5] ))
            self.conn.commit()
            self.conn.close()

        self.AddData_into_List.mainloop()

    def DataAdding(self):
        try:        
            AlbumDatalist = []
            with self.change_dir('my_BookData/Database'):
                self.conn = sqlite3.connect('Libraries.db')
                self.c = self.conn.cursor()

                self.c.execute(f"SELECT * FROM [{self.AlbumNamne}]")
                for t in self.c.fetchall():
                    AlbumDatalist.append(t[1])

                SelectData = self.listBook_Interface.focus()
                Data = self.listBook_Interface.item(SelectData, "values")
                AlbumData = str(Data[1])

                if AlbumData in AlbumDatalist:
                    tkinter.messagebox.showerror('Error', 'This book already added.')
                else:
                    if AlbumData != AlbumDatalist:
                        Data_Adding_to_Database = [
                                (
                                    Data[0], Data[1], Data[2], Data[3], Data[4], Data[5]
                                )
                            ]

                        self.c.executemany(f"INSERT INTO [{self.AlbumNamne}] VALUES (?,?,?,?,?,?) ", Data_Adding_to_Database)
                        self.conn.commit()
                self.conn.close()

        except IndexError as e:
            tkinter.messagebox.showwarning('Warning', 'Please Choose one file.')

    def DoneFunction(self):
        self.AddData_into_List.destroy()

    @contextmanager
    def change_dir(self, Destinetion):
        try:
            cwd = os.getcwd()
            os.chdir(Destinetion)
            yield
        finally:
            os.chdir(cwd)


#if __name__ == '__main__':
#    Adding_from_Library_into_Adlbum()