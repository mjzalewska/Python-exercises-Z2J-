from pathlib import Path
from PyPDF2 import PdfMerger

pdf_merger = PdfMerger()

# ### CONCATENATING PDF FILES ###
reports_dir = Path.home()/"Downloads"/"expense_reports"

# for path in reports_dir.glob("*.pdf"):
#     print(path.name)
# reports might not be printed in alphabetical order

expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()
# for path in expense_reports:
#     print(path.name)

# for path in expense_reports:
#     pdf_merger.append(str(path))
#
# with open("expense_reports.pdf", "wb") as output_file:
#     pdf_merger.write(output_file)

# quarterly_rep_dir = Path.home()/"Downloads"/"quarterly_report"
# toc_path = quarterly_rep_dir/"toc.pdf"
# rep_path = quarterly_rep_dir/"report.pdf"
#
# # step 1 - append pages to the pdf merger
# pdf_merger.append(str(rep_path))
# # step 2 - insert pages to be merged at the desired index
# pdf_merger.merge(1, str(toc_path))
#
# with open("full_report.pdf", "wb") as output:
#     pdf_merger.write(output)

# ### CONCAT. AND MERGING - REVIEW EXERCISES ###
# 1
files_dir = Path().home()/"Downloads"
files_for_merg = list(files_dir.glob("merge*.pdf"))
files_for_merg.sort()

for file in files_for_merg[:2]:
    pdf_merger.append(file)
with open("concatenated.pdf", "wb") as output_file:
    pdf_merger.write(output_file)

# 2
pdf_merger_m = PdfMerger()
concat_path = Path().cwd()/"concatenated.pdf"
pdf_merger_m.append(str(concat_path))
pdf_merger_m.merge(1, files_for_merg[2])

with open("merged.pdf", "wb") as output_file_m:
    pdf_merger_m.write(output_file_m)
