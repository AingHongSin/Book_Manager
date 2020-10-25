import os
import sqlite3

from tkinter import *
from tkinter import constants
from tkmacosx import Button
from contextlib import contextmanager

class RenameTable_and_AlbumData():
    def __init__(self, Album_Name):

        self.RenameWindow  = Toplevel()
        self.RenameWindow.title('Album Rename')
        #self.RenameWindow.geometry()
        self.RenameWindow.resizable(False, False)
        self.RenameWindow.config(background = '#00ebff')

        self.orgName = Album_Name

        self.AlbumVar = StringVar()

        # Frame
        self.TopFrame = Frame(self.RenameWindow, bg = '#00ebff')
        self.TopFrame.pack(side = 'top', fill  = 'x')

        self.mainFrame = LabelFrame(self.RenameWindow)
        self.mainFrame.pack(fill = 'x')

        self.BottomFrame = Frame(self.RenameWindow, bg = '#00ebff')
        self.BottomFrame.pack()
        
        # Interface
        self.lblTitle = Label(self.TopFrame, text = 'Album Rename', bg = '#00ebff', font = ('Times', 21, 'bold'))
        self.lblTitle.pack()

        self.lblAlbumName = Label(self.mainFrame, text = 'Album Name :', height = 5)
        self.lblAlbumName.grid(row = 0, column = 0)

        self.inpAlbumName = Entry(self.mainFrame, width = 20, textvariable = self.AlbumVar)
        self.inpAlbumName.grid(row = 0, column = 1)
        self.inpAlbumName.focus()
        self.inpAlbumName.insert(0, Album_Name)
        self.inpAlbumName.bind('<Return>', self.ReturnforDone)

        self.btnCancel = Button(self.BottomFrame, text = 'Cancel', borderless = 4, height = 30, command = self.RenameWindow.destroy)
        self.btnCancel.pack(side = 'left', padx = 5, pady = 5)

        self.btnDone = Button(self.BottomFrame, text = 'Done', borderless = 4, height = 30, command = self.Done_Backend_Processing)
        self.btnDone.pack(side = 'right', padx = 5, pady = 5)

        self.RenameWindow.mainloop()

    def ReturnforDone(self, event):
        self.Done_Backend_Processing()

    def Done_Backend_Processing(self):

        orgName = str(self.orgName)
        destinyName = self.AlbumVar.get()
        print("OGName :", orgName)
        print("AfterName :", destinyName)

        ONL = [orgName]
        DNL = [destinyName]
        rowID = []

        with self.change_dir('Database'):
           
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("SELECT rowid, * FROM Album WHERE Album_NameList = (?)", ONL)
            for item in self.c.fetchall():
                rowID.append(item[0])

            print(rowID[0])
            self.c.execute(f"UPDATE Album SET Album_NameList = (?) WHERE rowid = {rowID[0]} ", (DNL) ) 
            self.conn.commit()

            self.c.execute(f"ALTER TABLE [{orgName}] RENAME TO [{destinyName}]")
            self.conn.commit()
        
        self.conn.close()
        self.RenameWindow.destroy()



    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)
    



#if __name__ == '__main__':
#    RenameTable_and_AlbumData()
