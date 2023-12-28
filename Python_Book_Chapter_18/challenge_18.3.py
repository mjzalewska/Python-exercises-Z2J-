import easygui as gui
from PyPDF2 import PdfReader, PdfWriter


class PageExtractor:

    @classmethod
    def get_input_path(cls):
        input_file_path = gui.fileopenbox(title="Open file...", default="*.pdf")
        if input_file_path is None:
            exit()
        else:
            return input_file_path

    @classmethod
    def get_output_path(cls, input_file_path):
        while True:
            output_path = gui.filesavebox(title="Save file as...", default="*.pdf")
            if output_path is None:
                exit()
            else:
                if output_path == input_file_path:
                    gui.msgbox("You cannot overwrite the original file!")
                    continue
                else:
                    return output_path

    @classmethod
    def get_page_number(cls, start_pg_or_end_pg):
        while True:
            page = gui.enterbox(msg=f"Please enter {start_pg_or_end_pg} page number")
            if page is None:
                exit()
            else:
                if not page.isdigit():
                    gui.msgbox(msg="Please enter an integer value")
                else:
                    if int(page) < 0:
                        gui.msgbox(msg="Invalid page number! Please enter a positive integer")
                    else:
                        return int(page)-1

    @classmethod
    def extract_pages(cls, input_file_path, start_pg, end_pg):
        input_pdf = PdfReader(input_file_path)
        output_pdf = PdfWriter()

        for page in input_pdf.pages[start_pg:end_pg + 1]:
            output_pdf.add_page(page)

        return output_pdf

    @classmethod
    def save_file(cls, file, target_path):
        with open(target_path, "wb+") as output:
            file.write(output)


def run():
    page_extractor = PageExtractor()
    input_path = page_extractor.get_input_path()
    start_page = page_extractor.get_page_number("start")
    end_page = page_extractor.get_page_number("end")
    extracted_pages = page_extractor.extract_pages(input_path, start_page, end_page)
    page_extractor.save_file(extracted_pages, page_extractor.get_output_path(input_path))


if __name__ == "__main__":
    run()
