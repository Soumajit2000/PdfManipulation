import PyPDF2

input_file = 'super.pdf'
watermark_file = 'wtr.pdf'

pdf = PyPDF2.PdfFileReader(open(input_file, 'rb'))

watermark = PyPDF2.PdfFileReader(open(watermark_file, 'rb'))

output = PyPDF2.PdfFileWriter()

watermark_page = watermark.getPage(0)


for i in range(pdf.getNumPages()):
    page = pdf.getPage(i)
    page.mergePage(watermark_page)
    output.addPage(page)

with open('draft.pdf', 'wb') as file:
    output.write(file)
