"""Challenge 14.3 PdfFileSplitter Class

Create a class called PdfFileSplitter that reads a PDF from an existing PdfReader instance and splits the PDF into two
new PDFs. The class should be instantiated with a path string.
"""

from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader


class PdfFileSplitter:

    def __init__(self, source_path):
        self.path = list(Path().home().rglob(source_path))[0]
        self.writer_1 = None
        self.writer_2 = None

    def split(self, break_point):
        if break_point:
            try:
                pdf_reader = PdfReader(str(self.path))
                self.writer_1 = pdf_reader.pages[:break_point + 1]
                self.writer_2 = pdf_reader.pages[break_point:]

            except FileNotFoundError:
                file_name = str(self.path).split("\\")[-1]
                print(f"{file_name} has not been found or is a directory")

            except TimeoutError:
                print("The operation has timed out. Please try again")
        else:
            raise TypeError(f"Please provide the required positional argument: break_point")

    def write(self, target_file_name):
        if target_file_name:
            pdf_writer_1 = PdfWriter()
            pdf_writer_2 = PdfWriter()

            for page in self.writer_1:
                pdf_writer_1.add_page(page)
            with open(target_file_name + "_1.pdf", 'wb') as target_file_1:
                pdf_writer_1.write(target_file_1)

            for page in self.writer_2:
                pdf_writer_2.add_page(page)
            with open(target_file_name + "_2.pdf", 'wb') as target_file_2:
                pdf_writer_2.write(target_file_2)
        else:
            raise TypeError(f"Please provide the required positional argument: target_file_name")


pdf_splitter = PdfFileSplitter('Pride_and_Prejudice.pdf')
pdf_splitter.split(150)
pdf_splitter.write()
