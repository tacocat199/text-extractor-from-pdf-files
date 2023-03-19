import requests

url = 'https://raw.githubusercontent.com/tacocat199/text-extractor-from-pdf-files/main/input.text?token=GHSAT0AAAAAACAG2KJJT2RTPNIQHUZYC3R6ZAVZXNA'
response = requests.get(url)
text = response.content.decode('latin-1')

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
