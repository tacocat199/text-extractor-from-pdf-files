# reads text files from a specified folder path, decodes them using the 'latin-1' encoding, 
# and writes the decoded content to a single 'output.txt' file.
import os 
import requests

folder_path = 'F:\\projects\\text-extractor-from-pdf-files\\for_decoding'
output_file = 'output.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as file:
                content = file.read().decode('latin-1')
                f.write(content)
