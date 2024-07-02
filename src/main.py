from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

researched_text = pytesseract.image_to_string(Image.open('../test_images/jpn_img_part_drow.png'), lang='jpn')

print(researched_text)
print(len(researched_text))
