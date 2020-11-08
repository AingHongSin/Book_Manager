import os
import sqlite3
import datetime
import tkinter.dialog

import AuthorsFunction
import Convert_fomPdf_toImage


from PyPDF2 import PdfFileReader
from contextlib import contextmanager

class Extract_Metada_From_PDF():
    def __init__(self):
        
        self.datalist_of_Database = []

        
        # Database
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.c.execute("SELECT * FROM Data_list ")
            self.items = self.c.fetchall()

        with self.change_dir('my_BookData/Data'):
            self.dataFromDataFolder = os.listdir()

            for item in self.items:
                self.datalist_of_Database.append(item[1])

            self.Amount_Book = len(self.items) + 1

            PASSWORD = None

            for self.row in self.dataFromDataFolder:
                if self.row != '.DS_Store':
                    if self.row in self.datalist_of_Database:
                        print("", end="")
                    else:
                        pdf_path = str(self.row)
                        with open(pdf_path, 'rb') as f:
                            self.pdf = PdfFileReader(f)
                            if self.pdf.isEncrypted:
                                try:
                                    self.pdf.decrypt(PASSWORD)
                                except NotImplementedError:
                                    command = (f"qpdf --password='{PASSWORD}' --decrypt {self.row} {self.row};")
                                    os.system(command)            
                                    with open(pdf_path, mode='rb') as fp:
                                        self.pdf = PdfFileReader(fp)
                                        self.information = self.pdf.getDocumentInfo()
                                        self.number_of_pages = self.pdf.getNumPages()
                                            
                            self.information = self.pdf.getDocumentInfo()
                            self.number_of_pages = self.pdf.getNumPages()

                        ID = self.Amount_Book 
                        Title = str(self.row)
                        Author = (self.information.author)
                        Number_of_Pages = (self.number_of_pages)
                        Last_Read = (None)
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


                        os.chdir(os.path.dirname(os.getcwd()))
                        Convert_fomPdf_toImage.Splitting_and_Converting(pdf_path)
                        with self.change_dir('Database'): 
                            AuthorsFunction.Function(ID, Title, Author, Number_of_Pages, Last_Read, Add_Date)
                            
                        os.chdir('Data/')
                        
        self.conn.commit()
        self.conn.close()




    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)
