# from PIL import Image
# from pytesseract import pytesseract

# # Step 1: Open the image file
# image = Image.open('virustotal.png')

# # Step 2: Pre-process the image to enhance text recognition
# image = image.convert('RGB')

# # Step 3: Use Tesseract OCR to extract text from the image
# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# text = pytesseract.image_to_string(image)

# # Step 4: Print the extracted text
# print(text)

import requests
from bs4 import BeautifulSoup
import re

def is_malicious(url):
    try:
        response = requests.get(url)
        html_content = response.text
        
        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract text from the webpage
        text = soup.get_text()
        
        # Example: Check for known malicious patterns (you would need to define these)
        malicious_patterns = [
            'malware',
            'phishing',
            'virus',
            'attack'
        ]
        
        for pattern in malicious_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        
        return False
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

# Example usage:
url_to_check = 'https://example.com'
if is_malicious(url_to_check):
    print(f"{url_to_check} may be malicious.")
else:
    print(f"{url_to_check} appears to be safe.")
