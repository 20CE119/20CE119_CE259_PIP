#ID & Name   : 20CE119 DIPKUMAR RUPAPARA
#Aim         : Generate PDF file of your 3rd Semester Mark-sheet
#link(Github): https://github.com/20CE119/20CE119_CE259_PIP.git

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
pdf = PdfFileReader(str("20CE119.pdf"))
pdf_writer = PdfFileWriter()

print(pdf.getNumPages())
for page in pdf.pages:
    print(page.extractText())
    pdf_writer.addPage(page)

with Path("Result.pdf").open("wb") as output:
    pdf_writer.write(output)