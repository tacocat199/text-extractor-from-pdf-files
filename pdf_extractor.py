import PyPDF2

pdf_file = open('F:\pdf books\Spirituals, Psychology Books\Homer_ The Odyssey ( PDFDrive.com ).pdf', 'rb')
pdf_reader = PyPDF2.PdfileReader(pdf_file)

text = ''
for page in range(pdf_reader.getNumPages()):
    text += pdf_reader.getPage(page).extractText()

with open('input.text', 'w') as f:
    f.write(text)