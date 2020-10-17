from tkinter import *
from tkinter import ttk
from tkmacosx import Button

class DetailFunction():
    def __init__(self, Name, Title, Author, Creator, Producer, Subject, Number_of_pages):
        self.DetailViewerInterface = Toplevel()
        self.DetailViewerInterface.title("Book Detail")
        self.DetailViewerInterface.geometry('400x600+550+150')

        LabelName = ['Name :',
                    'Title :',
                    'Aurhor :',
                    'Creator :',
                    'Productor :',
                    'Subject :',
                    'Number of Page :'
                    ]

        Data = [
            Name,
            Title,
            Author,
            Creator,
            Producer,
            Subject,
            Number_of_pages
        ]
        
        self.TopFrame_DetailInterface = Frame(self.DetailViewerInterface)
        self.TopFrame_DetailInterface.pack(fill = 'x', side = 'top')
        self.TopFrame_DetailInterface.config(background = '#00EBFF')

        self.mainFrame_DetailInterface = Frame(self.DetailViewerInterface)
        self.mainFrame_DetailInterface.pack()



        self.bottomFrame_DetailInterface = Frame(self.DetailViewerInterface)
        self.bottomFrame_DetailInterface.pack(fill = 'x', side = 'bottom')
        
        self.lblDetailofBook = Label(self.TopFrame_DetailInterface, text = 'Book Detail', font = ('Times',24,'bold'), bg = '#00EBFF', fg = '#F0FFFF')
        self.lblDetailofBook.pack()

        for row in range(len(LabelName)):
            for col in range(row + 1):
                self.MessData = Message(self.mainFrame_DetailInterface, text = Data[col], width = 250)
                self.MessData.grid(row = col, column = 1, sticky = 'w')
            self.lblName = Label(self.mainFrame_DetailInterface, text = LabelName[row], height = 2)
            self.lblName.grid(row = row, column = 0, sticky = 'e')

        self.btnDone = Button(self.bottomFrame_DetailInterface, text = 'Done', borderless = 10, width = 100, height = 40, command = self.DetailViewerInterface.destroy)
        self.btnDone.pack(side = 'right', padx = 10, pady = 10) 

        self.DetailViewerInterface.mainloop()