import os
import PyPDF2

# Specify the folder path containing the PDF files
pdf_folder_path = 'F:\\projects\\text-extractor-from-pdf-files\\pdf_books'

# Specify the output file path for the decoded content
output_file_path = 'F:\\projects\\text-extractor-from-pdf-files\\data_meal\\input.txt'

# Open the output file in write mode
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Loop through each PDF file in the specified folder path
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, filename)
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ''
                for page in range(len(pdf_reader.pages)):
                    text += pdf_reader.pages[page].extract_text()
                # Remove excessive spacing
                text = ' '.join(text.split())
                # Write the extracted text to the output file
                output_file.write(text.strip() + '\n')
        