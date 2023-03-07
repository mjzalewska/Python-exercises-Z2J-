"""
Challenge 14.7 Unscramble a Pdf
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path().home()/"Downloads"/"scrambled.pdf"
pdf_reader = PdfReader(str(pdf_path))
pdf_writer = PdfWriter()

for i in range(len(pdf_reader.pages)):
    page_angle = pdf_reader.pages[i].get("/Rotate")
    if page_angle:
        pdf_reader.pages[i].rotate(-page_angle)
        pdf_writer.add_page(pdf_reader.pages[i])
    else:
        pdf_writer.add_page(pdf_reader.pages[i])

with open("unscrambled.pdf", "wb") as output_f:
    pdf_writer.write(output_f)







