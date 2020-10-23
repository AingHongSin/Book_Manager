from tkinter import *
from tkmacosx import Button


class AlbumEditing():
    def __init__(self):
        self.EditingAlbum_TopLevel = Tk()
        self.EditingAlbum_TopLevel.title("Album Edting")
        self.EditingAlbum_TopLevel.geometry("700x500+500+250")

        self.TopFrame = Frame(self.EditingAlbum_TopLevel, bg = '#00EBFF')
        self.TopFrame.pack(side = 'top')

        self.MainFrame = Frame(self.EditingAlbum_TopLevel)
        self.MainFrame.pack()


        self.EditingAlbum_TopLevel.mainloop()


if __name__ == "__main__":
    AlbumEditing()