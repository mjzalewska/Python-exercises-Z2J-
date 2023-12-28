import easygui as gui
from PyPDF2 import PdfReader, PdfWriter


def get_input_path():
    input_file_path = gui.fileopenbox(title="Choose file...", msg="Select a Pdf file to rotate...", default="*.pdf")
    if input_file_path is None:
        exit()
    else:
        return input_file_path


def get_rotation_deg():
    while True:
        degs = gui.buttonbox(title="Choose rotation...", msg="Please select rotation (degrees)",
                             choices=["90", "180", "270"])
        if degs is None:
            continue
        else:
            return int(degs)


def get_output_path(input_path):
    while True:
        output_path = gui.filesavebox(title="Save as...", default="*.pdf")
        if output_path is None:
            exit()
        else:
            if output_path == input_path:
                gui.msgbox(msg="Cannot overwrite original file!")
            else:
                return output_path


def rotate_pdf(input_file, rotation_degs):
    input_file = PdfReader(input_file)
    output_file = PdfWriter()

    # rotate all pages
    for page in input_file.pages:
        page = page.rotate(rotation_degs)
        output_file.add_page(page)

    return output_file


def save_output_file(file_obj, path):
    with open(path, "wb+") as output_file:
        file_obj.write(output_file)


pdf_input = get_input_path()
rotation = get_rotation_deg()
rotated_file = rotate_pdf(pdf_input, rotation)
save_output_file(rotated_file, get_output_path(pdf_input))
