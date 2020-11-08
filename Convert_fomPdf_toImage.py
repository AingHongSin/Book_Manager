# pdf_splitter.py
import os
from pdf2image import convert_from_path
from contextlib import contextmanager
from PyPDF2 import PdfFileReader, PdfFileWriter

class Splitting_and_Converting():
    def __init__(self, Name):

        with self.change_dir('Data'):
            path = Name
            self.pdf_splitter(path)

    def pdf_splitter(self, path):
        fname = os.path.splitext(os.path.basename(path))[0]

        pdf = PdfFileReader(path)
        for page in range(1):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
            output_filename = (path)

            os.chdir(os.path.dirname(os.getcwd()))
            with self.change_dir('splitting'):
                with open(output_filename, 'wb') as out:
                    pdf_writer.write(out)
            self.extractImageformPDF(path)

    def extractImageformPDF(self, Name):
        with self.change_dir('splitting'):
            file = Name
            pages = convert_from_path(file, 100)
            for page in range(1):
                os.chdir(os.path.dirname(os.getcwd()))
                with self.change_dir('Img'):
                    myfile = (os.getcwd() +'/'+ Name + '.png')
                    pages[page].save(myfile, "PNG")






    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)
