from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

pdf_path = (Path.home() / "Downloads" / "Pride_and_Prejudice.pdf")
pdf = PdfReader(str(pdf_path))

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


# # WRITING FILES TO TXT
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

# # WRITING FILES TO PDF
# pdf_writer = PdfWriter()
# page = pdf_writer.add_blank_page(width=72, height=72)  # width and height are measured in points (1 pt = 1/72 inch)
# OR
# pdf_writer.add_blank_page(width=72, height=72)

# with open(Path('blank.pdf'), 'wb') as f:
#     pdf_writer.write(f)

# Illustrative exercise #2 (extracting one page and saving it to an existing pdf file)

input_pdf = PdfReader(str(pdf_path))

# page = input_pdf.pages[0]
# new_pdf_writer = PdfWriter()
# # adds a page to the set of pages in the pdf writer but needs an existing pate obj:
# new_pdf_writer.add_page(page=page)
#
# with open('first page.pdf', 'wb') as f:
#     new_pdf_writer.write(f)

# Illustrative exercise #3 (extracting multiple pages and saving them to a new pdf file)
pdf_writer = PdfWriter()

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
pages = input_pdf.pages[1:4]
for page in pages:
    pdf_writer.add_page(page)

print(len(pdf_writer.pages))
with open('chapter 1 slice.pdf', 'wb') as destination_file:
    pdf_writer.write(destination_file)
