from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm  # importing standard units of measure
from reportlab.lib.pagesizes import LETTER  # importing statndard page formats (letter)
from reportlab.lib.colors import blue # import font color

canvas_a4 = Canvas("hello.pdf")
canvas_a4.drawString(72, 72, "Hello World")
# the first two arguments denote the distance from the left and bottom edge, respectively
# the values are measured in points, 1 pt = 1/72 of an inch
# the default page size is A4
# the default font is Helvetica size 12 pts
canvas_a4.save()

# SETTING PAGE SIZE
canvas_letter_sized = Canvas("hello_world.pdf", pagesize=(612.0, 792.0))  # letter-sized page
canvas_letter_sized.drawString(72, 720, "Hello World")
canvas_letter_sized.save()

# Using reportlab's units module to set the page size
canvas_conv_units = Canvas("hello_world_units.pdf", pagesize=(8, 5 * inch, 11 * inch))

# Using reportlab's standard page formats module to set the page size
canvas_standard_pg = Canvas("hello_world_standard.pdf", pagesize=LETTER)

# SETTING FONT

# three fonts available by default: Courier, Helvetica and Times New Roman
canvas_font = Canvas("font-example.pdf", pagesize=LETTER)
canvas_font.setFont("Times-Roman", 18)
canvas_font.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas_font.save()

# changing font color
canvas_color = Canvas("font-colors.pdf", pagesize=LETTER)
canvas_color.setFont("Times-Roman", 12)
canvas_color.setFillColor("blue")
canvas_color.drawString(1 * inch, 10 * inch, "Blue text")
canvas_color.save()

