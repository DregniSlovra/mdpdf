import imp
from re import T
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 50)

# create a cell
pdf.cell(200, 10, txt = "Test",
         ln = 1, align = 'C', fill=True)

pdf.line(10, 75, 390, 75)

# add another cell
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C')

# save the pdf with name .pdf
pdf.output("GFG.pdf")