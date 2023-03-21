import os
import PyPDF2

folder_path = 'F:\\projects\\text-extractor-from-pdf-files\\pdf_books'

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page].extract_text()
        with open(f'{filename}.txt', 'w') as txt_file:
            txt_file.write(text)

