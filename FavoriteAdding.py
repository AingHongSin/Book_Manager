import tkinter as tk
from tkinter import ttk
import sqlite3
import os

class FavoriteAdding_from_Library():
    def __init__(self):
        
        os.chdir('/Users/macbook/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.AddData_into_List = tk.Toplevel()

        self.topFrame = tk.Frame(self.AddData_into_List)
        self.topFrame.pack(side = 'top')

        self.lblTitle = tk.Label(self.topFrame, text = 'Add')

        self.mainFrame = tk.LabelFrame(self.AddData_into_List, text = 'Main List')
        self.mainFrame.pack()
        
        self.btnAdd  = tk.Button(self.mainFrame, text = 'Add', width = 10, command = self.DataAdding)
        self.btnAdd.pack(anchor = 'ne')

        self.btnDone = tk.Button(self.mainFrame, text = 'Done', width = 10, command = self.AddData_into_List.destroy)
        self.btnDone.pack(side = 'bottom')

        self.listBook_Interface = tk.ttk.Treeview(self.mainFrame, column = ('ID', 'Title', 'Author', 'Lenght', 'Category', 'Last Readed', 'Date Added'), show = 'headings', height = '10')
        self.listBook_Interface.pack(padx = '10', pady = '10')

        self.listBook_Interface.column('ID', width = '30')
        self.listBook_Interface.heading('ID', text = 'ID')

        self.listBook_Interface.column('Title', width = '180')
        self.listBook_Interface.heading('Title', text = 'Title')

        self.listBook_Interface.column('Author', width = '120')
        self.listBook_Interface.heading('Author', text = 'Author')

        self.listBook_Interface.column('Lenght', width = '50')
        self.listBook_Interface.heading('Lenght', text = 'Length')

        self.listBook_Interface.column('Category', width = '100')
        self.listBook_Interface.heading('Category', text = 'Category')

        self.listBook_Interface.column('Last Readed', width = '160')
        self.listBook_Interface.heading('Last Readed', text = 'Last Readed')

        self.listBook_Interface.column('Date Added', width = '160')
        self.listBook_Interface.heading('Date Added', text = 'Date Added')

        self.c.execute("SELECT * FROM Data_list ")
    
        self.items = self.c.fetchall()
    
        for item in self.items:
            if item[2] == None:
                self.listBook_Interface.insert("", tk.END, values = (item[0], item[1], 'Unknown Author', item[3],  item[4], item[5], item[6] ))
            else: 
                self.listBook_Interface.insert("", tk.END, values = (item[0], item[1], item[2], item[3],  item[4], item[5], item[6] ))
        
        self.AddData_into_List.mainloop()
    def DataAdding(self):
        
        os.chdir('/Users/macbook/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        SelectData = self.listBook_Interface.focus()
        Data = self.listBook_Interface.item(SelectData, "values")
        print(Data)

        Data_Adding_to_Database = [
                (
                    Data[0], Data[1], Data[2], Data[3], Data[4], Data[5], Data[6]
                )
            ]

        self.c.executemany(f"INSERT INTO Favorite VALUES (?,?,?,?,?,?,?) ", Data_Adding_to_Database)
        self.conn.commit()


