"""
Challenge 14.7 Unscramble a Pdf
"""
import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


class PdfUnscrambler:
    def __init__(self, path):
        self.path = path
        self.sep_files_path = Path().cwd() / "separate"
        self.reader_1 = None
        self.reader_2 = None
        self.pdf_writer_1 = None
        self.pdf_writer_2 = None
        self.pdf_merger = None

    def sort_pages(self):
        # split the document into pages
        reader_1 = PdfReader(self.path)
        Path.mkdir(self.sep_files_path, exist_ok=True)
        for i in range(len(reader_1.pages)):
            page = reader_1.pages[i]
            page_num = int(reader_1.pages[i].extract_text()[0])
            self.pdf_writer_1 = PdfWriter()
            self.pdf_writer_1.add_page(page)
            self._write(f"{self.sep_files_path}\\page_{str(page_num)}.pdf", self.pdf_writer_1)
        # sort and merge the pages
        folder_path = self.sep_files_path
        pdfs = list(folder_path.glob("*.pdf"))
        pdfs.sort()
        self.pdf_merger = PdfMerger()
        for path in pdfs:
            self.pdf_merger.append(str(path))
        self._merge("sorted.pdf", self.pdf_merger)

    def rotate_pages(self):
        self.reader_2 = PdfReader("sorted.pdf")
        self.pdf_writer_2 = PdfWriter()
        for i in range(len(self.reader_2.pages)):
            page_angle = self.reader_2.pages[i].get("/Rotate")
            if page_angle:
                self.reader_2.pages[i].rotate(-page_angle)
                self.pdf_writer_2.add_page(self.reader_2.pages[i])
            else:
                self.pdf_writer_2.add_page(self.reader_2.pages[i])
        self._write("unscrambled.pdf", self.pdf_writer_2)
        os.unlink("sorted.pdf")

    @staticmethod
    def _write(output_file_name, writer):
        with open(output_file_name, "wb") as output:
            writer.write(output)

    @staticmethod
    def _merge(output_file_name, merger):
        with open(output_file_name, "wb") as output:
            merger.write(output)


pdf_unscrambler = PdfUnscrambler("scrambled.pdf")
pdf_unscrambler.sort_pages()
pdf_unscrambler.rotate_pages()

