import copy
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# ### ROTATING PAGES ###

# pdf_path = Path().home() / "Downloads" / "ugly.pdf"

# pdf_reader = PdfReader(str(pdf_path))
# pdf_writer = PdfWriter()

# ### approach 1
# loop over indices of pages in the PDF and check if each index corresponds to a page that needs to
# be rotated. Then call .rotateClockwise() to rotate the page and add it to the pdf writer

# ok if you know ahead of time which pages need to be rotated

# for num in range(len(pdf_reader.pages)):
#     page = pdf_reader.pages[num]
#     if num % 2 == 0:  # even-numbered pages start at 0
#         page.rotate(90)
#         pdf_writer.add_page(page)
#
# with open("ugly_rotated.pdf", "wb") as target_file:
#     pdf_writer.write(target_file)

# ### approach 2

# pdf_reader_2 = PdfReader(str(pdf_path))
# page_1 = pdf_reader_2.pages[0]
# print(page_1["/Rotate"]) # the value is -90, i.e. page rotated counterclockwise by 90 degrees
#
# page_2 = pdf_reader_2.pages[1]
# print(page_2["/Rotate"]) # the value is 0, i.e. page not rotated

# pdf_reader_3 = PdfReader(str(pdf_path))
# pdf_writer_3 = PdfWriter()
#
# for page in pdf_reader_3.pages:
#     if page["/Rotate"] == -90:
#         page.rotate(90)
#     pdf_writer_3.add_page(page)
#
# # Things to look out for:
# # the Rotate key does not always exist on a page
# # when a paper doc is scanned to Pdf, the pages might be rotated but the /Rotate key might have the value zero
#
# with open("ugly_rotated_ver2.pdf", "wb") as target_file:
#     pdf_writer_3.write(target_file)

# ### CROPPING PAGES ###

# pdf_path = Path().home() / "Downloads" / "half_and_half.pdf"
# pdf_reader = PdfReader(str(pdf_path))
# pdf_writer = PdfWriter()
#
# first_page = pdf_reader.pages[0]
# print(first_page.mediabox)
# represents the rectangular area defining the boundries of the page
# RectangleObject([0, 0, 792, 612]) - measurement is points, i.e. 1/72 of an inch

# to get the coordinates of all page corners:
# print(first_page.mediabox.lower_left)
# print(first_page.mediabox.lower_right)
# print(first_page.mediabox.upper_left)
# print(first_page.mediabox.upper_right)

# to change the coordinates of a mediabox (this is effectively cropping the page):
# first_page.mediabox.upper_left = (0, 480)
# print(first_page.mediabox.upper_left)
# # the upper right adjusts automatically to preserve the rectangular shape:
# print(first_page.mediabox.upper_right)
#
# pdf_writer.add_page(first_page)
# with open("cropped_page", "wb") as target_file:
#     pdf_writer.write(target_file)

# ## To cut the page in half vertically
#
# pdf_reader_2 = PdfReader(str(pdf_path))
# pdf_writer_2 = PdfWriter()
#
# first_page = pdf_reader_2.pages[0]
#
# left_side = copy.deepcopy(first_page)
# current_coords = left_side.mediabox.upper_right
# # print(current_coords)
# new_coords = (int(current_coords[0]/2), current_coords[1])
#
# left_side.mediabox.upper_right = new_coords
#
# right_side = copy.deepcopy(first_page)
# right_side.mediabox.upper_left = new_coords
#
# pdf_writer_2.add_page(left_side)
# pdf_writer_2.add_page(right_side)
#
# with open("cropped_pages.pdf", "wb") as output:
#     pdf_writer_2.write(output)
#

# ## REVIEW EXERCISES ##
# 1

# pdf_path = Path().home()/"Downloads"/"split_and_rotate.pdf"
# pdf_reader = PdfReader(str(pdf_path))
# pdf_writer = PdfWriter()
#
# for page in pdf_reader.pages[::]:
#     if page["/Rotate"] == 90:
#         page.rotate(-90)
#     pdf_writer.add_page(page)
#
# with open("rotated.pdf", "wb") as output_f:
#     pdf_writer.write(output_f)

# 2
pdf_path = Path().home() / "PycharmProjects"/"Python-exercises-Z2J-"/"Python_Book_Chapter_14"/"rotated.pdf"
pdf_reader = PdfReader(str(pdf_path))

left_side_p1 = copy.deepcopy(pdf_reader.pages[0])
right_side_p1 = copy.deepcopy(pdf_reader.pages[0])
left_side_p2 = copy.deepcopy(pdf_reader.pages[1])
right_side_p2 = copy.deepcopy((pdf_reader.pages[1]))

current_coords = left_side_p1.mediabox.upper_right
new_coords = (current_coords[0]/2, current_coords[1])

left_side_p1.mediabox.upper_right = new_coords
right_side_p1.mediabox.upper_left = new_coords
left_side_p2.mediabox.upper_right = new_coords
right_side_p2.mediabox.upper_left = new_coords

pdf_writer = PdfWriter()
pdf_writer.add_page(left_side_p1)
pdf_writer.add_page(right_side_p1)
pdf_writer.add_page(left_side_p2)
pdf_writer.add_page(right_side_p2)

with open("split.pdf", "wb") as output:
    pdf_writer.write(output)



