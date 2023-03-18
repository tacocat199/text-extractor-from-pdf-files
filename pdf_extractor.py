import PyPDF2

pdf_file = open('Homer_The Odyssey_( PDFDrive.com).pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ''
for page in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page].extract_text()

with open('input.text', 'w') as f:
    f.write(text)