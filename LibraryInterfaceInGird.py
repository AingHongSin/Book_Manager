import os
import sqlite3


from tkinter import *
from tkmacosx import Button
from tkmacosx.widget import SFrame 
from PIL import Image, ImageTk
from contextlib import contextmanager


class Library_Interface_in_Gird_Function():
    def __init__(self, rightFrame_mainWindow):
        
        CoverBookName = []
                
        # Frame
        self.CoverBookFrame = SFrame(rightFrame_mainWindow, height = 650)
        self.CoverBookFrame.pack(fill = 'both', padx = 15, pady = 15)
        
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()
            
        with self.change_dir('my_BookData/Img'):
            for t in os.listdir():
                if t != '.DS_Store':
                    CoverBookName.append(t)

            for row in range(len(CoverBookName)):
                for Column in range(row):
                    self.AuthorPhoto_HomeInterface = PhotoImage(file = (os.getcwd() + "/" + CoverBookName[row] ))
                    #self.Name = CoverBookName[row]
                    self.AuthorPotho_image_HomeInterface = self.AuthorPhoto_HomeInterface.subsample(2,2)
                    self.btnAuthor_homeInterface = Button(self.CoverBookFrame, image = self.AuthorPotho_image_HomeInterface, activebackground = ('white'), borderless = 5, border = 0, borderwidth = 0, command = self.OpenFunction)
                    self.btnAuthor_homeInterface.config(width = 250)
                    self.btnAuthor_homeInterface.grid(row = row, column = Column, padx = 15, pady = 15)

            print("Done!")
            

        
        
    def OpenFunction(self):
        print('Name:' , self.Name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)
