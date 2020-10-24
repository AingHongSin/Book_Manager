import os
import io
import fitz
import PIL
#import pdf2image
#from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkmacosx import Button , SFrame
from contextlib import contextmanager

#import ImageExtraction

class DetailFunction():
    def __init__(self, Name, Title, Author, Creator, Producer, Subject, Number_of_pages, page_size):
        self.DetailViewerInterface = Toplevel()
        self.DetailViewerInterface.title("Book Detail")
        self.DetailViewerInterface.geometry('600x775+550+120')
        self.DetailViewerInterface.config(background = '#98F5FF')

        self.TopFrame_DetailInterface = Frame(self.DetailViewerInterface)
        self.TopFrame_DetailInterface.pack(fill = 'x', side = 'top')
        self.TopFrame_DetailInterface.config(background = '#00EBFF')

        self.SFrame = SFrame(self.DetailViewerInterface, width = 590, height = 700)
        self.SFrame.pack()

        self.PhotoFrame_DetailInterface = Frame(self.SFrame)
        self.PhotoFrame_DetailInterface.pack(fill = 'x', side = 'top', padx = 10, pady = 10)

        self.mainFrame_DetailInterface = Frame(self.SFrame)
        self.mainFrame_DetailInterface.pack()

        self.bottomFrame_DetailInterface = Frame(self.DetailViewerInterface, bg = '#98F5FF')
        self.bottomFrame_DetailInterface.pack(fill = 'x', side = 'bottom')

        self.lblDetailofBook = Label(self.TopFrame_DetailInterface, text = 'Book Detail', font = ('Times',24,'bold'), bg = '#00EBFF', fg = '#F0FFFF')
        self.lblDetailofBook.pack()

        with self.change_dir('Img'):
            Photo = PhotoImage(file = (os.getcwd() + "/" + str(Name)+ '.png'))
            Potho_image = Photo.subsample(2,2)

        self.lblPhoto_PhotoFrame = Label(self.PhotoFrame_DetailInterface, image = Potho_image, bg = 'red')
        self.lblPhoto_PhotoFrame.pack(side = 'top')
                         
        LabelName = [
                    'Name :',
                    'Title :',
                    'Aurhor :',
                    'Creator :',
                    'Productor :',
                    'Subject :',
                    'Number of Page :',
                    'page_size :'
                    ]

        Data = [
                Name,
                Title,
                Author,
                Creator,
                Producer,
                Subject,
                Number_of_pages,
                page_size
            ]
        
    
        for row in range(len(LabelName)):
            for col in range(row + 1):
                self.MessData = Message(self.mainFrame_DetailInterface, text = Data[col], width = 250)
                self.MessData.grid(row = col, column = 1, sticky = 'w')
            self.lblName = Label(self.mainFrame_DetailInterface, text = LabelName[row], height = 2)
            self.lblName.grid(row = row, column = 0, sticky = 'e')

        self.btnDone = Button(self.bottomFrame_DetailInterface, text = 'Done', borderless = 10, width = 100, height = 30, command = self.DetailViewerInterface.destroy)
        self.btnDone.pack(side = 'right', padx = 5, pady = 5)
        self.btnDone.focus()
        self.btnDone.bind('<Return>', self.Done) 

        self.DetailViewerInterface.mainloop()

    def Done(self, event):
        self.DetailViewerInterface.destroy()

    @contextmanager
    def change_dir(self, Destinetion):
        try:
            cwd = os.getcwd()
            os.chdir(Destinetion)
            yield
        finally:
            os.chdir(cwd)


