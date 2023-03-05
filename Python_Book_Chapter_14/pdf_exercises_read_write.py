from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# pdf_path = (Path.home() / "Downloads" / "Pride_and_Prejudice.pdf")
# pdf = PdfReader(str(pdf_path))

# # get number of pages
# print(len(pdf.pages))

# # get document info
# print(pdf.metadata)

# # access info like attribute
# print(pdf.metadata.title)

# # get page (Page object)
# print(pdf.pages[1])

# # get page text
# print(pdf.pages[0].extract_text())

# # iterate over pages in the file using the pages attribute
# for page in pdf.pages[0:4]:
#     print(page.extract_text())


# ### WRITING FILES TO TXT ###
# Illustrative example #1
# pdf_reader = PdfReader(str(pdf_path))
# output_pdf = Path.home() / "Downloads" / "Pride and Prejudice.txt"

# with open(output_pdf, 'w+') as file:
#     title = pdf_reader.metadata.title
#     num_pages = len(pdf_reader.pages)
#
#     file.write(f"{title}\nNumber of pages:{num_pages}\n\n")
#
#     for page in pdf_reader.pages:
#         text = page.extract_text()
#         file.write(text)

# with open(output_pdf, 'r') as file:
#     contents = file.read()
#     print(contents)

# Review exercise #1
# source_path = Path.home() / "Downloads" / "zen.pdf"
# pdf_source_file = PdfReader(str(source_path))
#
# # pages count
# print(len(pdf_source_file.pages))
# # print the first page
# print(pdf_source_file.pages[0].extract_text())

# ### WRITING FILES TO PDF ###
# pdf_writer = PdfWriter()
# page = pdf_writer.add_blank_page(width=72, height=72)  # width and height are measured in points (1 pt = 1/72 inch)
# OR
# pdf_writer.add_blank_page(width=72, height=72)

# with open(Path('blank.pdf'), 'wb') as f:
#     pdf_writer.write(f)

# Illustrative exercise #2 (extracting one page and saving it to an existing pdf file)

# input_pdf = PdfReader(str(pdf_path))

# page = input_pdf.pages[0]
# new_pdf_writer = PdfWriter()
# # adds a page to the set of pages in the pdf writer but needs an existing pate obj:
# new_pdf_writer.add_page(page=page)
#
# with open('first page.pdf', 'wb') as f:
#     new_pdf_writer.write(f)

# Illustrative exercise #3 (extracting multiple pages and saving them to a new pdf file)
# pdf_writer = PdfWriter()

# ver_1
# for n in range(1, 4):
#     page = input_pdf.pages[n]
#     pdf_writer.add_page(page=page)
#
# print(len(pdf_writer.pages))
#
# with open('chapter 1.pdf', 'wb') as output:
#     pdf_writer.write(output)
#
# ver_2
# pages = input_pdf.pages[1:4]
# for page in pages:
#     pdf_writer.add_page(page)
#
# print(len(pdf_writer.pages))
# with open('chapter 1 slice.pdf', 'wb') as destination_file:
#     pdf_writer.write(destination_file)
#
# Read all pages from and write to a pdf file
# pdf_writer.append_pages_from_reader(input_pdf)
# print(len(pdf_writer.pages))
# with open('Pride and Prejudice.pdf', 'wb') as destination_file:
#     pdf_writer.write(destination_file)


# Review exercises (Writing files to pdf)

## 1
# source_path = Path.home() / "Downloads" / "Pride_and_Prejudice.pdf"
# pdf_reader = PdfReader(str(source_path))
# pdf_writer = PdfWriter()

# last_page = pdf_reader.pages[len(pdf_reader.pages) - 1]
# pdf_writer.add_page(last_page)
# with open('last_page.pdf', 'wb') as file:
#     pdf_writer.write(file)

## 2
# source_path = Path.home()/"Downloads"/"Pride_and_Prejudice.pdf"
# pdf_reader = PdfReader(str(source_path))
# pdf_writer = PdfWriter()
# even_pages = pdf_reader.pages[0:len(pdf_reader.pages) - 1:2]
# # alternatively even_pages = pdf_reader.pages[::2]
# for page in even_pages:
#     pdf_writer.add_page(page)
#
# with open('evey_other_page.pdf', 'wb') as dest_file:
#     pdf_writer.write(dest_file)

## 3
source_path = Path.home() / "Downloads" / "Pride_and_Prejudice.pdf"
pdf_reader = PdfReader(str(source_path))
pdf_writer_1 = PdfWriter()
pdf_writer_2 = PdfWriter()
first_part = pdf_reader.pages[:151]
second_part = pdf_reader.pages[151:]

for page in first_part:
    pdf_writer_1.add_page(page)
with open('part_1.pdf', 'wb') as first_file:
    pdf_writer_1.write(first_file)

for page in second_part:
    pdf_writer_2.add_page(page)
with open('part_2.pdf', 'wb') as second_file:
    pdf_writer_2.write(second_file)
