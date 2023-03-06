from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

# ### ENCRYPTING PDF FILES ###

# pdf_path = Path().home()/"Downloads"/"newsletter.pdf"
#
# pdf_reader = PdfReader(str(pdf_path))
# pdf_writer = PdfWriter()
# pdf_writer.append_pages_from_reader(pdf_reader)
#
# user_pass = "SuperSecret"
# owner_pass = "ReallySuperSecret"
# pdf_writer.encrypt(user_password=user_pass, owner_password=owner_pass)
# # if only user_password is set the owner_pwd defaults to the same string
#
# with open("newsletter_protected.pdf", "wb") as output:
#     pdf_writer.write(output)

# ### DECRYPTING PDF FILES ###

# as long as a file is not decrypted it's impossible to open in in Python as well - an error will be thrown
# new_pdf_path = Path.home()/"PycharmProjects"/"Python-exercises-Z2J-"/"Python_Book_Chapter_14"/"newsletter_protected.pdf"
# new_pdf_reader = PdfReader(str(new_pdf_path))
# new_pdf_reader.decrypt(password="ReallySuperSecret")
# 0 - password incorrect
# 1 - user password matched
# 2 - owner password matched

# ### REVIEW EXERCISES ###

# 1
# pdf_path = Path().home()/"Downloads"/"top_secret.pdf"
# pdf_reader = PdfReader(str(pdf_path))
# pdf_writer = PdfWriter()
#
# pdf_writer.append_pages_from_reader(pdf_reader)
# user_pass = "Unguessable"
# pdf_writer.encrypt(user_password=user_pass)
#
# with open("top_secret_encrypter.pdf", "wb") as output:
#     pdf_writer.write(output)

# 2

pdf_path = Path().home()/"PycharmProjects"/"Python-exercises-Z2J-"/"Python_Book_Chapter_14"/"top_secret_encrypter.pdf"
pdf_reader = PdfReader(str(pdf_path))
user_pass = "Unguessable"
pdf_reader.decrypt(password=user_pass)

print(pdf_reader.pages[0].extract_text())
